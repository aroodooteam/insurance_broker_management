# -*- coding: utf-8 -*-


from openerp import api, exceptions, fields, models, _


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'
    _description = 'Add broker to policy'

    broker_line_ids = fields.One2many(comodel_name='analytic.broker.line', inverse_name='analytic_id', string='Broker Line')
