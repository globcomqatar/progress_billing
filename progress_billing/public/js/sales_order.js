frappe.ui.form.on("Sales Order", {
	refresh(frm) {
		render_progress_billing_summary(frm);
		add_create_progress_invoice_button(frm);
	},
	pb_billing_method(frm) {
		render_progress_billing_summary(frm);
	},
});

function render_progress_billing_summary(frm) {
	if (frm.doc.pb_billing_method !== "Progress Billing") {
		frm.set_df_property("pb_progress_billing_summary", "options", "");
		return;
	}

	const grand_total = flt(frm.doc.grand_total);
	const per_billed = flt(frm.doc.per_billed);
	const billed_amount = (grand_total * per_billed) / 100;
	const remaining_amount = grand_total - billed_amount;
	const remaining_percent = 100 - per_billed;

	const html = `
		<table class="table table-bordered" style="margin-bottom: 0;">
			<tr><td>${__("Total Contract Value")}</td><td>${format_currency(grand_total, frm.doc.currency)}</td></tr>
			<tr><td>${__("Total Progress Billed")}</td><td>${format_currency(billed_amount, frm.doc.currency)} (${per_billed.toFixed(2)}%)</td></tr>
			<tr><td>${__("Remaining Amount")}</td><td>${format_currency(remaining_amount, frm.doc.currency)} (${remaining_percent.toFixed(2)}%)</td></tr>
		</table>
	`;
	frm.set_df_property("pb_progress_billing_summary", "options", html);
	frm.refresh_field("pb_progress_billing_summary");
}

function add_create_progress_invoice_button(frm) {
	if (
		frm.doc.docstatus !== 1 ||
		frm.doc.pb_billing_method !== "Progress Billing" ||
		flt(frm.doc.per_billed) >= 100
	) {
		return;
	}

	frm.add_custom_button(
		__("Create Progress Invoice"),
		() => show_progress_invoice_dialog(frm),
		__("Create")
	);
}

function show_progress_invoice_dialog(frm) {
	const remaining_percent = 100 - flt(frm.doc.per_billed);

	const dialog = new frappe.ui.Dialog({
		title: __("Create Progress Invoice"),
		fields: [
			{
				fieldname: "remaining_percent",
				fieldtype: "Percent",
				label: __("Remaining Percentage"),
				default: remaining_percent,
				read_only: 1,
			},
			{
				fieldname: "percentage",
				fieldtype: "Percent",
				label: __("Billing Percentage"),
				reqd: 1,
			},
		],
		primary_action_label: __("Create Invoice"),
		primary_action(values) {
			if (values.percentage <= 0 || values.percentage > remaining_percent + 0.01) {
				frappe.msgprint(
					__("Billing Percentage must be greater than 0 and not exceed the remaining {0}%.", [
						remaining_percent.toFixed(2),
					])
				);
				return;
			}

			frappe.call({
				method: "progress_billing.api.create_progress_invoice",
				args: {
					sales_order: frm.doc.name,
					percentage: values.percentage,
				},
				freeze: true,
				freeze_message: __("Creating Progress Invoice..."),
				callback(r) {
					if (!r.exc && r.message) {
						dialog.hide();
						frappe.model.sync(r.message);
						frappe.set_route("Form", r.message.doctype, r.message.name);
					}
				},
			});
		},
	});

	dialog.show();
}
