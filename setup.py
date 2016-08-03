# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('sprypy/spry.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "spry",
    packages = ["sprypy"],
    entry_points = {
        "console_scripts": ['spry = sprypy.spry:main']
        },
    version = version,
    description = "social media scanner",
    long_description = long_descr,
    author = "James A. Campbell",
    author_email = "james@jamescampbell.us",
    url = "https://github.com/jamesacampbell/spry",
    download_url = "https://github.com/jamesacampbell/spry/tarball/0.2.4",
keywords = ['social', 'collector', 'scraper'], # arbitrary keywords
  classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    )
