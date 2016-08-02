from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
setup(
  name = 'spry',
  license='GNUv3',
  version = '0.1.8',
  description = 'Spry is a social media collector toolsuite',
  author = 'James Campbell',
  author_email = 'james@jamescampbell.us',
  url = 'https://github.com/jamesacampbell/spry', # use the URL to the github repo
  download_url = 'https://github.com/jamesacampbell/spry/tarball/0.1.8',

  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Programming Language :: Python',],
      packages=["spry", "spry.modules"],
    package_data={'spry': ['sociallist/sociallist.txt']},
  install_requires = ['requests>=1.0'],

    entry_points={
        'console_scripts': [
            'spry=spry.spry:main',
        ],
    },

)
