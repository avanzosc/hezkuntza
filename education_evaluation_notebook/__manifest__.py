# Copyright 2019 Adrian Revilla - Avanzosc S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Education Evaluation Notebook",
    "version": "12.0.7.0.0",
    "category": "Education",
    "depends": [
        "education",
        "contacts_school",
        "contacts_school_education",
        "mail",
        "portal",
        "hr_school",
        "hr_education",
        "report_xlsx",
        "queue_job",
    ],
    "author":  "AvanzoSC",
    "license": "AGPL-3",
    "website": "http://www.avanzosc.es",
    "data": [
        "security/ir.model.access.csv",
        "security/education_evaluation_notebook_rules.xml",
        "data/education_evaluation_notebook_data.xml",
        "reports/education_group_exam_report_view.xml",
        "reports/education_group_homework_report_view.xml",
        "reports/education_group_student_exam_report_view.xml",
        "reports/education_group_student_homework_report_view.xml",
        "reports/education_record_all_xlsx_report_view.xml",
        "reports/education_record_xlsx_report_view.xml",
        "reports/res_partner_record_xlsx_report_view.xml",
        "views/education_academic_year_evaluation_view.xml",
        "views/education_competence_type_view.xml",
        "views/education_competence_view.xml",
        "views/education_course_change_view.xml",
        "views/education_exam_type_view.xml",
        "views/education_exam_view.xml",
        "views/education_group_view.xml",
        "views/education_homework_view.xml",
        "views/education_mark_behaviour_view.xml",
        "views/education_mark_numeric_view.xml",
        "views/education_schedule_view.xml",
        "views/education_notebook_line_view.xml",
        "views/education_notebook_template_view.xml",
        "views/education_record_view.xml",
        "views/hr_employee_view.xml",
        "views/res_partner_view.xml",
        "wizards/create_academic_year_evaluation_view.xml",
        "wizards/export_education_record_xlsx_report_view.xml",
        "views/education_notebook_menu_view.xml",
        "views/report_partner_record_template.xml",
    ],
    "installable": True,
}
