
from odoo import models, fields

class phongban(models.Model):
    _name = 'ql.pb'
    _description = 'PhongBan'
    _rec_name = 'ten'

    ma = fields.Char('ID', size=50, required=True)
    ten = fields.Char('Name', size=225, required=True)
    mota = fields.Text('Describe', size=1000)
    manytomany = fields.Many2many('ql.nv',string="Add Employee")
