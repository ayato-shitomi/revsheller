from setuptools import setup, find_packages
import revsheller

DESCRIPTION = "revsheller - Easy to generate reverse shells and build a server"
NAME = 'revsheller'
AUTHOR = 'Ayato Shitomi'
AUTHOR_EMAIL = 'ioiaao.stmyt@gmail.com'
URL = 'https://github.com/ayato-shitomi/revsheller'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/ayato-shitomi/revsheller'
VERSION = revsheller.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
]

PACKAGES = [
	'revsheller'
]

CLASSIFIERS = [
	'Intended Audience :: System Administrators',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.8',
	'Programming Language :: Python :: 3.9',
	'Topic :: Scientific/Engineering',
	'Topic :: Security',
]

with open('README.md', 'r') as fp:
	readme = fp.read()

setup(name=NAME,
	author=AUTHOR,
	author_email=AUTHOR_EMAIL,
	maintainer=AUTHOR,
	maintainer_email=AUTHOR_EMAIL,
	description=DESCRIPTION,
	long_description=readme,
	long_description_content_type='text/markdown',
	license=LICENSE,
	url=URL,
	version=VERSION,
	download_url=DOWNLOAD_URL,
	python_requires=PYTHON_REQUIRES,
	install_requires=INSTALL_REQUIRES,
	packages=PACKAGES,
	classifiers=CLASSIFIERS
)
