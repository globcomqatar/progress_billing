import frappe
from frappe.tests.utils import FrappeTestCase


class TestCustomFields(FrappeTestCase):
	def test_sales_order_fields_exist(self):
		meta = frappe.get_meta("Sales Order")
		self.assertTrue(meta.has_field("pb_billing_method"))
		self.assertTrue(meta.has_field("pb_progress_billing_status"))
		self.assertTrue(meta.has_field("pb_progress_billing_summary"))

		billing_method_field = meta.get_field("pb_billing_method")
		self.assertEqual(billing_method_field.fieldtype, "Select")
		self.assertEqual(billing_method_field.default, "Quantity Based")
		self.assertEqual(billing_method_field.options, "Quantity Based\nProgress Billing")

	def test_sales_invoice_fields_exist(self):
		meta = frappe.get_meta("Sales Invoice")
		self.assertTrue(meta.has_field("pb_is_progress_invoice"))
		self.assertTrue(meta.has_field("pb_progress_billing_percentage"))
		self.assertTrue(meta.has_field("pb_against_sales_order"))

		against_so_field = meta.get_field("pb_against_sales_order")
		self.assertEqual(against_so_field.fieldtype, "Link")
		self.assertEqual(against_so_field.options, "Sales Order")
