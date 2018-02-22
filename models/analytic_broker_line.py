# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import Warning
from openerp.addons.decimal_precision import decimal_precision as dp
import logging
logger = logging.getLogger(__name__)


class AnalyticBrokerLine(models.Model):
    _name = 'analytic.broker.line'
    _description = 'Broker of contract'

    name = fields.Many2one(comodel_name='res.partner', string='Broker', domain="[('is_broker', '=', True)]", help='List of broker')
    analytic_id = fields.Many2one(comodel_name='account.analytic.account', string='Policy')

