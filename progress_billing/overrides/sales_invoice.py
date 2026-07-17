import frappe
from frappe import _
from frappe.utils import flt


def update_progress_billing_status(doc, method):
	sales_orders = {item.sales_order for item in doc.items if item.sales_order}

	for so_name in sales_orders:
		billing_method = frappe.db.get_value("Sales Order", so_name, "pb_billing_method")
		if billing_method != "Progress Billing":
			continue

		per_billed = flt(frappe.db.get_value("Sales Order", so_name, "per_billed"))
		status = "Completed" if per_billed >= 99.99 else "In Progress"
		frappe.db.set_value("Sales Order", so_name, "pb_progress_billing_status", status)


def validate_is_progress_invoice(doc, method):
	if doc.is_return:
		return

	sales_orders = {item.sales_order for item in doc.items if item.sales_order}

	for so_name in sales_orders:
		billing_method = frappe.db.get_value("Sales Order", so_name, "pb_billing_method")
		if billing_method == "Progress Billing" and not doc.pb_is_progress_invoice:
			frappe.throw(
				_(
					"Sales Order {0} uses Progress Billing. Use 'Create Progress Invoice' "
					"on the Sales Order instead of a standard invoice."
				).format(so_name)
			)
