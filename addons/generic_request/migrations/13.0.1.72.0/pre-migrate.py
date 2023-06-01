from odoo.addons.generic_mixin.tools.migration_utils import ensure_version


@ensure_version('1.72.0')
def migrate(cr, installed_version):
    cr.execute("""
        INSERT INTO ir_model_data
                (name, model, module, res_id, noupdate)
        SELECT 'request_stage_type_progress',
               'request.stage.type',
               'generic_request',
               id,
               True
        FROM request_stage_type
        WHERE code = 'progress'
    """)
