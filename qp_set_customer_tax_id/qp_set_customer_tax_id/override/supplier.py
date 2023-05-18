import re
import frappe
from frappe import _
from erpnext.buying.doctype.supplier.supplier import Supplier


class QlipSupplier(Supplier):

    def autoname(self):
        print("--------------------qlip---------------------")
        supp_master_name = frappe.defaults.get_global_default('supp_master_name')
        if supp_master_name == 'Supplier Name':
            self.name = self.get_supplier_name()
        else:
            set_name_by_naming_series(self)

    def get_supplier_name(self):

        return self.tax_id
