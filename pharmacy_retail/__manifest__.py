{
    'name': 'Pharmacy',
    'version': '1.0',
    'category': 'Health and Fitness',
    'description': """
This setup is for pharmacy retail companies that purchase and sell products.
They maintain the stock lot wise and also manage the expiry of the lots.
""",
    'depends': [
        'calendar',
        'contacts',
        'knowledge',
        'point_of_sale',
        'product_expiry',
        'product_margin',
        'purchase_stock',
        'sale_loyalty',
        'sale_margin',
        'sale_purchase',
        'sale_stock',
        'web_studio',
    ],
    'data': [
        'data/stock_location.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
        'data/product_category.xml',
        'data/res_partner.xml',
        'data/product_tag.xml',
        'data/pos_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/pos_config.xml',
        'data/stock_putaway_rule.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/res_config_settings.xml',
        'data/ir_model_data.xml',
        'data/mail_message.xml',
    ],
    'demo': [
        'demo/res_partner_title.xml',
        'demo/res_partner.xml',
        'demo/stock_lot.xml',
        'demo/product_supplierinfo.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_reward.xml',
        'demo/loyalty_rule.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_post.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/loyalty_generate_wizard.xml',
        'demo/sale_loyalty_wizard.xml',
        'demo/sale_order_post.xml',
        'demo/payment_provider_demo_post.xml',
        'demo/payment_provider.xml',
        'demo/payment_method.xml',
        'demo/pos_payment_method.xml',
        'demo/pos_config.xml',
    ],
    'license': 'OPL-1',
    'author': 'Odoo S.A.',
    'images': ['images/main.png'],
}
