# -*-coding: utf-8 -*-

from odoo import models, fields,api

class thoigian(models.Model):
    _name = 'ql.times'
    _description = 'ThoiGian'
    _rec_name = 'tutal'

    start = fields.Date('Start date', size=10,default='2000-01-01')
    end = fields.Date('End date', size=10,default='2020-01-01')
    manytomany = fields.Many2one('ql.nv','Department',required=True)
    manytomany1 = fields.Many2one('ql.pb','Employee',required=True)
    tutal = fields.Char(compute='_tutalString')

    @api.multi
    @api.depends('manytomany', 'manytomany1')
    def _tutalString(self):
        for record in self:
            if record.manytomany and record.manytomany1:
                record.tutal = record.manytomany.name + record.manytomany1.ten
