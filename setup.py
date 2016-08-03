# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup, find_packages
#from distutils.core import setup

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
    entry_points = {
        "console_scripts": ['spry = spry:main']
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
