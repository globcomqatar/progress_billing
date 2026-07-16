app_name = "progress_billing"
app_title = "Progress Billing"
app_publisher = "Globcom Qatar"
app_description = "Percentage-of-contract-value progress invoicing for ERPNext Sales Orders"
app_email = "waheed@globcomqatar.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "progress_billing",
# 		"logo": "/assets/progress_billing/logo.png",
# 		"title": "Progress Billing",
# 		"route": "/progress_billing",
# 		"has_permission": "progress_billing.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/progress_billing/css/progress_billing.css"
# app_include_js = "/assets/progress_billing/js/progress_billing.js"

# include js, css files in header of web template
# web_include_css = "/assets/progress_billing/css/progress_billing.css"
# web_include_js = "/assets/progress_billing/js/progress_billing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "progress_billing/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "progress_billing/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "progress_billing.utils.jinja_methods",
# 	"filters": "progress_billing.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "progress_billing.install.before_install"
# after_install = "progress_billing.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "progress_billing.uninstall.before_uninstall"
# after_uninstall = "progress_billing.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "progress_billing.utils.before_app_install"
# after_app_install = "progress_billing.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "progress_billing.utils.before_app_uninstall"
# after_app_uninstall = "progress_billing.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "progress_billing.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"progress_billing.tasks.all"
# 	],
# 	"daily": [
# 		"progress_billing.tasks.daily"
# 	],
# 	"hourly": [
# 		"progress_billing.tasks.hourly"
# 	],
# 	"weekly": [
# 		"progress_billing.tasks.weekly"
# 	],
# 	"monthly": [
# 		"progress_billing.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "progress_billing.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "progress_billing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "progress_billing.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["progress_billing.utils.before_request"]
# after_request = ["progress_billing.utils.after_request"]

# Job Events
# ----------
# before_job = ["progress_billing.utils.before_job"]
# after_job = ["progress_billing.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"progress_billing.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

