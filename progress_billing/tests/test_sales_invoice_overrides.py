import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import flt
from erpnext.selling.doctype.sales_order.test_sales_order import make_sales_order

from progress_billing.api import create_progress_invoice

# This test site does not have the standard ERPNext test fixtures (_Test Customer,
# _Test Item, _Test Warehouse - _TC, etc.) preloaded. Declaring test_dependencies
# forces frappe's test runner to create them (recursively, via each doctype's
# test_records.json) before this module's tests run. See erpnext's own
# test_sales_order.py for the same idiom (test_dependencies = ["Currency Exchange"]).
test_dependencies = ["Customer", "Item", "Warehouse"]


class TestProgressBillingStatusSync(FrappeTestCase):
	def make_progress_so(self):
		so = make_sales_order(
			item_list=[{"item_code": "_Test Item", "qty": 1, "rate": 100000}],
			do_not_submit=True,
		)
		so.pb_billing_method = "Progress Billing"
		so.save()
		so.submit()
		return so

	def test_status_flips_to_completed_at_100_percent(self):
		so = self.make_progress_so()

		invoice = frappe.get_doc(create_progress_invoice(so.name, 100))
		invoice.insert()
		invoice.submit()

		so.reload()
		self.assertEqual(so.pb_progress_billing_status, "Completed")

	def test_status_stays_in_progress_below_100(self):
		so = self.make_progress_so()

		invoice = frappe.get_doc(create_progress_invoice(so.name, 40))
		invoice.insert()
		invoice.submit()

		so.reload()
		self.assertEqual(so.pb_progress_billing_status, "In Progress")

	def test_status_reverts_to_in_progress_on_cancel(self):
		so = self.make_progress_so()

		invoice = frappe.get_doc(create_progress_invoice(so.name, 100))
		invoice.insert()
		invoice.submit()

		invoice.cancel()

		so.reload()
		self.assertEqual(flt(so.per_billed), 0.0)
		self.assertEqual(so.pb_progress_billing_status, "In Progress")

	def test_standard_invoice_blocked_against_progress_billing_order(self):
		so = self.make_progress_so()

		invoice = frappe.new_doc("Sales Invoice")
		invoice.customer = so.customer
		invoice.company = so.company
		invoice.currency = so.currency
		invoice.append(
			"items",
			{
				"item_code": "_Test Item",
				"qty": 1,
				"rate": 100000,
				"sales_order": so.name,
			},
		)

		with self.assertRaises(frappe.ValidationError):
			invoice.insert()

	def test_progress_invoice_not_blocked(self):
		so = self.make_progress_so()

		invoice = frappe.get_doc(create_progress_invoice(so.name, 10))
		invoice.insert()  # should not raise
		self.assertTrue(invoice.name)

	def test_standard_invoice_allowed_against_quantity_based_order(self):
		so = make_sales_order(
			item_list=[{"item_code": "_Test Item", "qty": 1, "rate": 100000}],
			do_not_submit=True,
		)
		so.submit()

		invoice = frappe.new_doc("Sales Invoice")
		invoice.customer = so.customer
		invoice.company = so.company
		invoice.currency = so.currency
		invoice.append(
			"items",
			{
				"item_code": "_Test Item",
				"qty": 1,
				"rate": 100000,
				"sales_order": so.name,
			},
		)
		invoice.insert()  # should not raise
		self.assertTrue(invoice.name)
