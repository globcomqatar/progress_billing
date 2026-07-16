import frappe
from frappe import _


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
