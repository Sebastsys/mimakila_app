from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mimakila_app/__init__.py
from mimakila_app import __version__ as version

setup(
	name="mimakila_app",
	version=version,
	description="Software elaborado para control de produccion de una fabrica",
	author="Francisco Adame",
	author_email="sebas.franksys@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
