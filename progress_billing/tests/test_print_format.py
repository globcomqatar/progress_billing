import frappe
from frappe.tests.utils import FrappeTestCase


class TestProgressBillingSummaryPrintFormat(FrappeTestCase):
	def test_print_format_exists_for_sales_order(self):
		meta = frappe.get_doc("Print Format", "Progress Billing Summary")
		self.assertEqual(meta.doc_type, "Sales Order")
		self.assertEqual(meta.print_format_type, "Jinja")
		self.assertIn("pb_progress_billing_log", meta.html)
