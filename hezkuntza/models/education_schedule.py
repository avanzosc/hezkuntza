# Copyright 2020 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class EducationSchedule(models.Model):
    _inherit = 'education.schedule'

    center_id = fields.Many2one(
        domain=[('educational_category', '=', 'school')])
