import re
import frappe
from frappe import _
from erpnext.selling.doctype.customer.customer import Customer


class QlipCustomer(Customer):

    def get_customer_name(self):

        return self.tax_id
