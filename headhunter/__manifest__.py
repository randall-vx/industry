{
    'name': 'Talent Acquisition',
    'version': '1.0',
    'category': 'Services',
    'description': """
This setup is for Talent Acquisition Agency / Recruitment Agency / Staffing Agency.
Those agencies work on two levels and with two different audiences, ...
""",
    'depends': [
        'account',
        'appointment_crm',
        'appointment_hr_recruitment',
        'base_automation',
        'crm_enterprise',
        'documents_hr_recruitment',
        'documents_product',
        'knowledge',
        'sign',
        'sale_crm',
        'web_studio',
        'website_appointment',
        'website_crm',
        'website_hr_recruitment',
    ],
    'data': [
        'data/base_automation.xml',
        'data/mail_template.xml',
        'data/ir_actions_server.xml',
        'data/hr_recruitment_stage.xml',
        'data/ir_model_fields.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_view.xml',
        'data/product_product.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/appointment_type.xml',
        'data/hr_department.xml',
        'data/hr_job.xml',
        'data/ir_attachment_post.xml',
        'data/sign_template.xml',
        'data/sign_item.xml',
        'data/sign_request.xml',
        'data/crm_stage.xml',
        'data/crm_tag.xml',
        'data/website_view.xml',
        'data/ir_model_data.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/calendar_event.xml',
        'demo/website.xml',
        'demo/crm_lead.xml',
        'demo/hr_job.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/website_ir_attachment.xml',
        'demo/website_view.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
        'demo/hr_candidate.xml',
        'demo/hr_applicant.xml',
    ],
    'license': 'OPL-1',
    'author': 'Odoo S.A.',
    'images': ['images/main.png'],
}
