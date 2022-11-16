# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployee(models.Model):

    _inherit = "hr.employee"

    hours_to_work = fields.Float(string="Hours to Work", help="""Expected working hours based on company policy. This is used \
             on attendance sheets to calculate overtime values.""",)

    use_attendance_sheets = fields.Boolean(string="Use Attendance Sheets",
        help="""Used in the attendance sheet auto creation process. Employees \
             that have the 'Hourly' type will have attendance sheets \
             automatically created""",)

    attendance_admin = fields.Many2one("hr.employee", string="Attendance Admin",
        help="""In addition to the employees manager, this person can
        administer attendances for all employees in the department. This field
        is set on the department.""",
        related="department_id.attendance_admin",)


class HrEmployeePublic(models.Model):

    _inherit = "hr.employee.public"

    hours_to_work = fields.Float(string="Hours to Work",
        help="""Expected working hours based on company policy. This is used \
             on attendance sheets to calculate overtime values.""",)

    use_attendance_sheets = fields.Boolean(string="Use Attendance Sheets",
        help="""Used in the attendance sheet auto creation process. Employees \
             that have the 'Hourly' type will have attendance sheets \
             automatically created""",)

    attendance_admin = fields.Many2one("hr.employee",
        string="Attendance Admin",
        help="""In addition to the employees manager, this person can
        administer attendances for all employees in the department. This field
        is set on the department.""",
        related="department_id.attendance_admin",)
