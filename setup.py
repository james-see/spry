from distutils.core import setup
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
setup(
  name = 'spry',
  packages = ['spry'], # this must be the same as the name above
  version = '0.1.5',
  description = 'Spry is a social media collector toolsuite',
  author = 'James Campbell',
  author_email = 'james@jamescampbell.us',
  url = 'https://github.com/jamesacampbell/spry', # use the URL to the github repo
  download_url = 'https://github.com/jamesacampbell/spry/tarball/0.1.5',

  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Programming Language :: Python',],
)
