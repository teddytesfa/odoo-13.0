import logging
from odoo import api, SUPERUSER_ID
from odoo.addons.generic_mixin.tools.migration_utils import ensure_version

_logger = logging.getLogger(__name__)


@ensure_version('1.29.0')
def migrate(cr, installed_version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    for request in env['request.request'].search([]):
        try:
            request._request_bind_attachments()
        except Exception:
            _logger.warning(
                "Cannot bind attachments for request %s",
                request, exc_info=True)
