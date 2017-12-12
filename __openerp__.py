# -*- coding: utf-8 -*-

{
    "name": "Insurance Broker Management",
    "version": "0.1",
    "author": "Haritiana Maminiaina Rakotomalala <hmrakotomalala@aro.mg>",
    "category": "Insurance",
    "complexity": "normal",
    "data": [
        # "data/templates.xml", # un comment to enable js, css code
        # "security/security.xml",
        # "security/ir.model.access.csv",
        "views/analytic_history_view.xml",
        "views/analytic_history_broker_line_view.xml",
        # "actions/act_window.xml",
        # "menu.xml",
        # "data/data.xml",
    ],
    "depends": [
        "base",
        "insurance_management",
    ],
    "qweb": [
        # "static/src/xml/*.xml",
    ],
    "test": [
    ],
    "installable": True,
    "auto_install": False,
}
