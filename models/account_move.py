from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    fecha_pago = fields.Date(
        string='Fecha del último pago',
        compute='_compute_fecha_pago',
        store=True,
        help='Fecha del último pago registrado para esta factura, aunque no esté completamente pagada'
    )
    
    @api.depends('line_ids.matched_debit_ids', 'line_ids.matched_credit_ids')
    def _compute_fecha_pago(self):
        for move in self:
            # Obtener todos los pagos reconciliados con esta factura
            reconciled_payments = move._get_reconciled_payments()
            
            if reconciled_payments:
                # Ordenar por fecha descendente y tomar la más reciente
                last_payment = reconciled_payments.sorted('date', reverse=True)[0]
                move.fecha_pago = last_payment.date
            else:
                move.fecha_pago = False