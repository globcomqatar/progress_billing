# Progress Billing

Adds percentage-of-contract-value invoicing to ERPNext Sales Orders, for
industries that bill by contract completion percentage (EPC, industrial
manufacturing, construction, engineering projects) rather than item
quantity.

## Install

    bench get-app progress_billing /path/to/apps/progress_billing
    bench --site your-site.local install-app progress_billing

## Usage

1. On a Sales Order, set **Billing Method** to **Progress Billing** before
   or after submit.
2. Submit the Sales Order.
3. Use **Create > Create Progress Invoice**, enter a billing percentage,
   and a draft Sales Invoice is generated with every line's rate scaled to
   that percentage (quantity is left unchanged).
4. Repeat until 100% is billed — **Progress Billing Status** on the Sales
   Order then flips to **Completed**.
5. See the **Progress Billing Summary** report for a cross-order view of
   contract value, percentage billed, and remaining amount.

## Scope

Out of scope for v1: named milestone billing schedules, per-item
percentage overrides, retention/holdback handling. See
`docs/superpowers/specs/2026-07-16-progress-billing-design.md` in the
planning repo for the full design rationale.
