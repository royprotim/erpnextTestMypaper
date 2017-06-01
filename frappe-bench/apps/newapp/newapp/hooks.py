# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "newapp"
app_title = "NewApp"
app_publisher = "royprotim"
app_description = "Configuration for custom apps"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "demo@testing.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/newapp/css/newapp.css"
# app_include_js = "/assets/newapp/js/newapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/newapp/css/newapp.css"
# web_include_js = "/assets/newapp/js/newapp.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "newapp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "newapp.install.before_install"
# after_install = "newapp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "newapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Payment Entry 2": "newapp.newapp.newapp.payment_entry_2.set_branch",
# 	"Payment Entry": "newapp.newapp.newapp.payment_entry_2.set_branch",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Payment Entry 2": {
# 		"validate": "newapp.newapp.newapp.payment_entry_2.set_branch"
# 	},
# 	"Payment Entry": {
# 		"validate": "newapp.newapp.newapp.payment_entry_2.set_branch"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"newapp.tasks.all"
# 	],
# 	"daily": [
# 		"newapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"newapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"newapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"newapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "newapp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "newapp.event.get_events"
# }

