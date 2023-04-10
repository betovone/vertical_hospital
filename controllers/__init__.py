# -*- coding: utf-8 -*-

from . import controllers
from odoo import http

def register_routes(cr, registry):
    http_routing = http.routing.Route
    for route in controllers.routes:
        http_routing(route[0], **route[1]).register()
