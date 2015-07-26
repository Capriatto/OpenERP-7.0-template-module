#!/usr/bin/env python
# -*- coding: utf-8 -*-

{
	'name' : 'SAC: OPA',
	'version' : '1.0',
	'depends' : ['base','crm', 'sac_configuracion', 'sac_reportes'],
	'author' : 'zeta',
	'category' : 'CRM',
	'description' : """Modulo de configuracion""",
	'website' : 'http://zeta.net.co/',
	'data' : [
		'views/view_crm_case.xml',
		'views/view_crm_case_section.xml',
		'views/sac_crm_lead_productos_view.xml',
		'views/sac_crm_oportunity_view.xml',
		'views/sac_crm_lead_phone_view.xml',
		'data/smtp.sql',
	],
	'qweb': ['static/src/xml/custom_access_login.xml'],
    'css': ['static/src/css/custom_login.css','static/src/css/custom_field.css'],
	'installable' : True
}
