``SPRY SPY PRY SPRY SPY PRY SPRY``

.. image:: https://img.shields.io/pypi/v/spry.svg
    :target: https://pypi.python.org/pypi/spry
.. image:: https://badges.gitter.im/Join%20Chat.svg
   :target:  https://gitter.im/sprypy/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. image:: https://readthedocs.org/projects/spry/badge/?version=latest
   :target: http://spry.rtfd.io
   
social media intelligence from the terminal
-----------------------------------------------

WORKING SCREENSHOT (version 0.4.9)

.. image:: https://cloud.githubusercontent.com/assets/616585/17407123/259d637c-5a34-11e6-96b1-0ef1b82a9559.png

WARNING:
********
this is in early beta

30 social accounts working so far...

KEY FEATURES:
=============

1. Saves profile images and content from each profile found in the directory that you ran the command from.
2. Puts all found data into a single PDF (username-report.pdf) in the directory that you ran the command from.
3. Progress DOTS and nice COLOURS assuming your terminal supports it.
4. Randomized pausing between lookups so you don't get blocked.
5. Randomized list of +8500 User Agent strings in use by default (can override via -u arg).
6. Proxy override via -p arg.

INSTALL via pip:
================

``pip install spry``

or

INSTALL via git:
================

``git clone git@github.com:jamesacampbell/spry.git``

then ``cd spry`` then ``python spry-run.py [username]``

DEV PATH?

the goal is to get to +100 services that have public url user name profile links to check and gather information from

EXAMPLES:
=========

run via ``spry [username]``

run without spitting out a pdf report:

``spry [username] --no-report``

run with verbose mode (show the user agent of each request):

``spry [username] -v``


