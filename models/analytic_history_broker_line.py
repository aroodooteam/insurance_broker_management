# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import Warning
from openerp.addons.decimal_precision import decimal_precision as dp
import logging
logger = logging.getLogger(__name__)


class AnalyticHistoryBrokerLine(models.Model):
    _name = 'analytic_history.broker.line'
    _description = 'Broker of contract version'

    name = fields.Many2one(comodel_name='res.partner', string='Broker', domain="[('is_broker', '=', True)]", help='List of broker')
    rate = fields.Float(string='Rate', digits_compute=dp.get_precision('Account'), help='Rate for broker')
    amount = fields.Float(string='Amount', digits_compute=dp.get_precision('Account'), help='Fixed amount for broker')
    history_id = fields.Many2one(comodel_name='analytic.history', string='History')

