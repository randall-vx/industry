{
    'name': 'Handyman Services',
    'version': '1.0',
    'category': 'Services',
    'description': "",
    'depends': [
        'account_accountant',
        'appointment_account_payment',
        'hr',
        'industry_fsm_sale_report',
        'industry_fsm_stock',
        'knowledge',
        'project_purchase',
        'project_timesheet_forecast_sale',
        'sale_crm',
        'sale_purchase_stock',
        'spreadsheet_sale_management',
        'web_studio',
    ],
    'data': [
        'data/res_config_setting.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/ir_actions_server.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_view.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/planning_role.xml',
        'data/project_task_type.xml',
        'data/project_project.xml',
        'data/product_product.xml',
        'data/sale_order_spreadsheet.xml',
        'data/sale_order_template.xml',
        'data/sale_order_template_line.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/crm_lead.xml',
        'demo/mail_activity.xml',
        'demo/hr_employee.xml',
        'demo/planning_recurrency.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/planning_slot_template.xml',
        'demo/planning_slot.xml',
        'demo/product_supplierinfo.xml',
        'demo/account_analytic_line.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'handyman/static/src/js/my_tour.js',
        ],
    },
    'author': 'Odoo S.A.',
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
    ],
    'images': ['images/main.png'],
}
