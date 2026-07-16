import frappe
from frappe import _


def validate_billing_method_lock(doc, method):
	if doc.is_new():
		return

	previous = doc.get_doc_before_save()
	if not previous or previous.pb_billing_method == doc.pb_billing_method:
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
