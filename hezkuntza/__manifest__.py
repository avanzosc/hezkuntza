# Copyright 2019 Oihane Crucelaegui - AvanzOSC4
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Hezkuntza",
    "version": "12.0.4.0.0",
    "category": "Education",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "depends": [
        "education",
        "resource_education",
        "hr_education",
        "hr_contract_education",
        "contacts_school",
        "partner_second_lastname",
        # "excel_import_export",
    ],
    "data": [
        "data/education_group_type_data.xml",
        "data/education_plan_data.xml",
        "data/education_subject_type_data.xml",
        "security/hezkuntza_groups.xml",
        "views/education_academic_year_view.xml",
        "views/education_activity_type_view.xml",
        "views/education_contract_type_view.xml",
        "views/education_course_view.xml",
        "views/education_designation_level_view.xml",
        "views/education_field_view.xml",
        "views/education_group_type_view.xml",
        "views/education_idtype_view.xml",
        "views/education_language_view.xml",
        "views/education_level_view.xml",
        "views/education_model_view.xml",
        "views/education_plan_view.xml",
        "views/education_position_view.xml",
        "views/education_shift_view.xml",
        "views/education_subject_view.xml",
        "views/education_task_type_view.xml",
        "views/education_work_reason_view.xml",
        "views/education_workday_type_view.xml",
        "wizard/update_education_partner_view.xml",
        "wizard/upload_education_activity_type_view.xml",
        "wizard/upload_education_all_view.xml",
        "wizard/upload_education_classroom_view.xml",
        "wizard/upload_education_contract_type_view.xml",
        "wizard/upload_education_course_view.xml",
        "wizard/upload_education_designation_level_view.xml",
        "wizard/upload_education_field_view.xml",
        "wizard/upload_education_group_view.xml",
        "wizard/upload_education_group_type_view.xml",
        "wizard/upload_education_idtype_view.xml",
        "wizard/upload_education_language_view.xml",
        "wizard/upload_education_level_view.xml",
        "wizard/upload_education_level_course_subject_view.xml",
        "wizard/upload_education_level_field_subject_view.xml",
        "wizard/upload_education_level_task_type_view.xml",
        "wizard/upload_education_level_workday_type_view.xml",
        "wizard/upload_education_model_view.xml",
        "wizard/upload_education_position_view.xml",
        "wizard/upload_education_resource_view.xml",
        "wizard/upload_education_schedule_view.xml",
        "wizard/upload_education_shift_view.xml",
        "wizard/upload_education_student_view.xml",
        "wizard/upload_education_subject_view.xml",
        "wizard/upload_education_task_type_view.xml",
        "wizard/upload_education_teacher_view.xml",
        "wizard/upload_education_work_reason_view.xml",
        "wizard/upload_education_workday_type_view.xml",
        "views/hezkuntza_menu_view.xml",
    ],
    'external_dependencies': {
        'python': [
            'chardet',
        ],
    },
    "installable": True,
    "application": True,
}
