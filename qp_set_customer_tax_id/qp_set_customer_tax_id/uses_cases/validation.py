import frappe
from frappe import _


def handle(documento, method):

    # Garantizar que el tax_id no se repita

        duplicado = frappe.db.sql("""
		select tax_id from tab{0}
        where tax_id = {1}
        and name != {2}""".format(documento.doctype, documento.tax_id, documento.name), as_dict=True)

        print("duplicado", duplicado)
        if duplicado:
            frappe.throw(_("Duplicate {0} found in the table").format(documento.tax_id))
