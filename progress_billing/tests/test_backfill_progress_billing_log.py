import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import flt
from erpnext.selling.doctype.sales_order.test_sales_order import make_sales_order

from progress_billing.api import create_progress_invoice
from progress_billing.patches.v1_1.backfill_progress_billing_log import execute


class TestBackfillProgressBillingLog(FrappeTestCase):
	test_dependencies = ["Customer", "Item", "Warehouse"]

	def make_progress_so_with_invoice_but_no_log_row(self):
		so = make_sales_order(
			item_list=[{"item_code": "_Test Item", "qty": 1, "rate": 100000}],
			do_not_submit=True,
		)
		so.pb_billing_method = "Progress Billing"
		so.save()
		so.submit()

		invoice = frappe.get_doc(create_progress_invoice(so.name, 100))
		invoice.currency = so.currency
		invoice.insert()
		invoice.submit()

		# Simulate "data from before this upgrade": the invoice exists and is
		# submitted (so.sync_progress_billing_log_row already logged it via
		# Task 3's real-time hook), but we clear the log to reproduce the
		# pre-upgrade state the patch needs to backfill.
		so.reload()
		so.pb_progress_billing_log = []
		so.save(ignore_permissions=True)

		return so, invoice

	def test_backfill_creates_log_row_for_existing_invoice(self):
		so, invoice = self.make_progress_so_with_invoice_but_no_log_row()

		execute()

		so.reload()
		self.assertEqual(len(so.pb_progress_billing_log), 1)
		row = so.pb_progress_billing_log[0]
		self.assertEqual(row.sales_invoice, invoice.name)
		self.assertEqual(row.progress_no, 1)
		self.assertEqual(row.invoice_status, "Submitted")

	def test_backfill_is_idempotent(self):
		so, invoice = self.make_progress_so_with_invoice_but_no_log_row()

		execute()
		execute()

		so.reload()
		self.assertEqual(len(so.pb_progress_billing_log), 1)
