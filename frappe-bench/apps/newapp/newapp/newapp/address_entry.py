from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document

class Address(Document):
	pass

@frappe.whitelist()
def get_address_from_pin(pin):
	add = frappe.get_doc("Pincode Master",{"pincode":pin})
	A = {}
	A['city']=add.division_name
	A['state']=add.state_name
	return json.dumps(A)

@frappe.whitelist()
def get_address_from_pin_for_pincodeMaster(pin):
	add = frappe.get_doc("Pincode Master",{"pincode":pin})
	A = {}
	A['division_name']=add.division_name
	A['state_name']=add.state_name
	A['region_name']=add.region_name
	A['circle_name']=add.circle_name
	A['taluk']=add.taluk
	A['district_name']=add.district_name
	return json.dumps(A)