# -*-coding: utf-8 -*-

from odoo import models, fields

class nhanvien(models.Model):
    _name = 'ql.nv'
    _description = 'NhanVien'
    _rec_name = 'name'

    ma = fields.Char('ID', size=50, required=True)
    name = fields.Char('Name', size=225, required=True)
    mota = fields.Text('Describe', size=1000)
    email = fields.Char('Email', size=30)
    diachi = fields.Text('Address',size=500)
    ngaysinh = fields.Date('Birth', size=10,default='01/01/1970')
    gioitinh = fields.Selection([('m','man'), ('w','woman')],'Sex',default='m')
    cmtnd = fields.Char('People ID', size=12 )

    pbid= fields.Many2one('ql.pb','Department')
    manytomany = fields.Many2many('ql.pb',string="Add Department")