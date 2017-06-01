# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document

class PaymentEntry2(Document):
	def validate(self):
		self.branch = set_branch(self.bank_details)

@frappe.whitelist()
def set_branch(ifsc):
	bank = frappe.get_doc("Bank Master",ifsc)
	B = {}
	B['city']=bank.city
	B['branch']=bank.branch
	B['micr']=bank.micr
	B['state']=bank.state
	B['contact']=bank.contact
	B['bank_name']=bank.bank_name
	return json.dumps(B)

@frappe.whitelist()
def get_data_from_micr(micr):
	bank = frappe.get_doc("Bank Master",{"micr":(micr)})
	B = {}
	B['ifsc_code']=bank.ifsc_code
	return json.dumps(B)