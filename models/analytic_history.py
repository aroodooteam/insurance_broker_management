# -*- coding: utf-8 -*-


from openerp import api, exceptions, fields, models, _


class AnalyticHistory(models.Model):
    _inherit = 'analytic.history'
    _description = 'History of the policy'

    broker_line_ids = fields.One2many(comodel_name='analytic_history.broker.line', inverse_name='history_id', string='Broker Line')
