# Copyright 2021 Creu Blanca
# Copyright 2023 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _recompute_tax_lines(
        self, recompute_tax_base_amount=False, tax_rep_lines_to_recompute=None
    ):
        # As we cannot pass the date, we have to use context
        super(
            AccountMove,
            self.with_context(
                vat_prorate_date=self.date or self.invoice_date or fields.Date.today()
            ),
        )._recompute_tax_lines(
            recompute_tax_base_amount=recompute_tax_base_amount,
            tax_rep_lines_to_recompute=tax_rep_lines_to_recompute,
        )

    @api.model
    def _get_tax_grouping_key_from_base_line(self, base_line, tax_vals):
        # We need to set the right account and analytic info for prorate lines. They
        # will be marked as 'vat_prorate'
        result = super()._get_tax_grouping_key_from_base_line(base_line, tax_vals)
        result["vat_prorate"] = tax_vals.get("vat_prorate", False)
        if result["vat_prorate"]:
            result["account_id"] = (
                base_line.company_id._get_tax_prorrate_account_map().get(
                    base_line.account_id.user_type_id.id
                )
                or base_line.account_id.id
            )
            result["analytic_account_id"] = base_line.analytic_account_id.id
            result["analytic_tag_ids"] = [(6, 0, base_line.analytic_tag_ids.ids or [])]
        return result

    @api.model
    def _get_tax_grouping_key_from_tax_line(self, tax_line):
        result = super()._get_tax_grouping_key_from_tax_line(tax_line)
        result["vat_prorate"] = tax_line.vat_prorate
        return result

    @api.onchange("invoice_line_ids")
    def _onchange_invoice_line_ids(self):
        """If we change any analytic information, we should drop all the taxes lines
        for forcing a recreation of them, as only on creation, the analytic information
        is transferred.

        It has to be done here, as if putting any onchange at invoice line level, the
        changes in other lines are not transferred when returning.

        This means a bit of overhead, from both executing this more times than strictly
        needed, and removing some stuff, but there's no other way. Anyway, the impact is
        minimized doing it only if the invoice company has prorate, and removing only
        the lines for the affected taxes.

        """
        if self.company_id.with_vat_prorate:
            vat_prorate_lines = self.line_ids.filtered("vat_prorate")
            tax_repartition_lines = vat_prorate_lines.tax_repartition_line_id
            self.line_ids -= self.line_ids.filtered(
                lambda x: x.tax_repartition_line_id in tax_repartition_lines
            )
        return super()._onchange_invoice_line_ids()

    def _reverse_move_vals(self, default_values, cancel=True):
        """Reassign again the proper field name on prorate lines after avoiding the
        account reassignation in super (in combination with `copy_data` method in
        account.move.line).
        """
        self = self.with_context(prorrate_refund=True)
        vals = super()._reverse_move_vals(default_values, cancel=cancel)
        for command in vals["line_ids"]:
            line_vals = command[2]
            if line_vals.get("prorate_tax_repartition_line_id"):
                line_vals["tax_repartition_line_id"] = line_vals.pop(
                    "prorate_tax_repartition_line_id"
                )
        return vals


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    vat_prorate = fields.Boolean()

    def _process_aeat_tax_fee_info(self, res, tax, sign):
        super()._process_aeat_tax_fee_info(res, tax, sign)
        if self.vat_prorate:
            res[tax]["deductible_amount"] -= self.balance * sign

    def copy_data(self, default=None):
        """Move `tax_repartition_line_id` value to other field name for avoiding the
        `account_id` reassignation due to the code inside `_reverse_move_vals`, which
        calls this one. We will put it again after, overwriting the other method.
        """
        res = super().copy_data(default=default)
        if self.env.context.get("prorrate_refund"):
            for vals in res:
                if vals.get("vat_prorate") and vals.get("tax_repartition_line_id"):
                    repartition_line_id = vals.pop("tax_repartition_line_id")
                    vals["prorate_tax_repartition_line_id"] = repartition_line_id
        return res
