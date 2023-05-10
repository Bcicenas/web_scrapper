from setuptools import find_packages, setup

setup(
	name='web_scrapper',
	version='1.0.0',
	packages=find_packages(),
	include_package_data=True,
	install_requires=[
		'kivy==2.1.0',
		'beautifulsoup4==4.12.2',
		'urllib3==1.26.15'
	],

)
