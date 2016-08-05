# -*- coding: utf-8 -*-
# spry social media scanner
#
# Spry is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Spry is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Spry. If not, see <http://www.gnu.org/licenses/>.

import re
from setuptools import setup, find_packages
#from distutils.core import setup
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('spry/spry.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "spry",
    packages = ['spry','spry.modules'],
    install_requires=[
          'requests', # the best way to load URLS
          'clint', # to do the cool dots while waiting
          'fpdf', # to generate a PDF report!
          'bs4', # to parse data from profile pages
          'termcolor', # for fun colours!
          'pysocks', # for tor proxy support
      ],
      license = "GNU",
    entry_points = {
        "console_scripts": ['spry = spry.spry:main']
        },
    version = version,
    description = "social media scanner",
    long_description = long_descr,
    author = "James A. Campbell",
    author_email = "james@jamescampbell.us",
    url = "https://github.com/jamesacampbell/spry",
    download_url = "https://github.com/jamesacampbell/spry/tarball/"+version,
keywords = ['social', 'collector', 'scraper'], # arbitrary keywords
  classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Programming Language :: Python',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    )
