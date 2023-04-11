from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in qp_set_customer_tax_id/__init__.py
from qp_set_customer_tax_id import __version__ as version

setup(
	name='qp_set_customer_tax_id',
	version=version,
	description='Qp Set Customer Tax Id',
	author='Mentum',
	author_email='aryrosa.fuentes@MENTUM.group',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
