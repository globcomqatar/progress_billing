import frappe
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
