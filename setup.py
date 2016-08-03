from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

def readme():
    with open('README.rst') as f:
        return f.read()
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
setup(
  include_package_data=True,
  name = 'spry',
  license='GNUv3',
  version = '0.2.1',
  description = 'Spry is a social media collector toolsuite',
  long_description = readme(),
  author = 'James Campbell',
  author_email = 'james@jamescampbell.us',
  url = 'https://github.com/jamesacampbell/spry', # use the URL to the github repo
  download_url = 'https://github.com/jamesacampbell/spry/tarball/0.2.1',

  keywords = ['social', 'collector', 'scraper'], # arbitrary keywords
  classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',],
      packages=["sprypy", "sprypy.modules",],
  install_requires = ['requests>=1.0',],
    entry_points={
        'console_scripts': [ 'spry=sprypy.spry:main',],
        }
)
