# Copyright (C) 2019 - TODAY, Patrick Wilson
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Field Service - Generic Request",
    "summary": "Create field service orders from a Request",
    "version": "13.0.1.0.1",
    "license": "AGPL-3",
    "author": "Pavlov Media, Odoo Community Association (OCA)",
    "category": "Request",
    "website": "https://github.com/OCA/field-service",
    "depends": ["fieldservice", "generic_request"],
    "data": [
        "views/request_views.xml",
        "views/fsm_order_views.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
