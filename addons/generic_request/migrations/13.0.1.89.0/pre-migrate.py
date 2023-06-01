from odoo.addons.generic_mixin.tools.migration_utils import ensure_version


@ensure_version('1.89.0')
def migrate(cr, installed_version):
    cr.execute("""
        -- Update view for users form to avoid migration errors
        UPDATE ir_ui_view
        SET arch_db = replace(
               arch_db,
               '<field name="related_request_count"/>',
               '<field name="total_request_count"/>')
        WHERE id IN (
            SELECT res_id
            FROM ir_model_data
            WHERE model = 'ir.ui.view'
              AND module = 'generic_request'
              AND name = 'view_users_form');
    """)
