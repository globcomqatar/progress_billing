import frappe
from frappe import _
from frappe.utils import flt


def refresh_progress_billing_log_payments(doc, method):
	for row in doc.get("pb_progress_billing_log") or []:
		if not row.sales_invoice:
			continue

		invoice = frappe.db.get_value(
			"Sales Invoice",
			row.sales_invoice,
			["grand_total", "outstanding_amount"],
			as_dict=True,
		)
		if not invoice:
			continue

		row.amount_paid = flt(invoice.grand_total) - flt(invoice.outstanding_amount)
		row.outstanding_amount = flt(invoice.outstanding_amount)
		row.payment_percentage = (
			(row.amount_paid / invoice.grand_total * 100) if invoice.grand_total else 0
		)


def validate_billing_method_lock(doc, method):
	if doc.is_new():
		return

	# frappe.db.get_value (not doc.get_doc_before_save()) so this works
	# identically whether Frappe fires us via "validate" (draft save) or
	# "before_update_after_submit" (editing a submitted order) — the latter
	# is required because pb_billing_method has allow_on_submit=1.
	previous_billing_method = frappe.db.get_value("Sales Order", doc.name, "pb_billing_method")
	if previous_billing_method == doc.pb_billing_method:
		return

	has_progress_invoice = frappe.db.exists(
		"Sales Invoice",
		{"pb_against_sales_order": doc.name, "docstatus": 1},
	)
	if has_progress_invoice:
		frappe.throw(
			_(
				"Billing Method cannot be changed because Progress Invoices already exist against this Sales Order."
			)
		)
