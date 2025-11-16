``SPRY SPY PRY SPRY SPY PRY SPRY``

.. image:: https://img.shields.io/pypi/v/spry.svg
    :target: https://pypi.python.org/pypi/spry
.. image:: https://badges.gitter.im/Join%20Chat.svg
   :target:  https://gitter.im/sprypy/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. image:: https://readthedocs.org/projects/spry/badge/?version=latest
   :target: http://spry.rtfd.io
   
social media intelligence from the terminal
-----------------------------------------------

Version 0.5.6 - Major Update:

- **Upgraded to Python 3.12+** (supports 3.12, 3.13, 3.14)
- **Migrated to uv** - Fast Python package manager (10-100x faster than pip)
- **Modernized codebase** - Removed Python 2 compatibility, modern Python 3 syntax
- **Enhanced Instagram detection** - Improved profile image extraction and error handling
- **Better PDF reports** - Now includes full list of found accounts with clickable links
- **SSL error handling** - Gracefully handles sites with certificate issues
- **Wayback Machine support** - Checks archived versions of dead sites (Myspace, Delicious, etc.)
- **Updated URLs** - Twitter now uses x.com

Requires Python 3.12 or higher.

WORKING SCREENSHOT (version 0.5.6)

.. image:: https://cloud.githubusercontent.com/assets/616585/17407123/259d637c-5a34-11e6-96b1-0ef1b82a9559.png

WARNING:
********
this is in early beta

30+ social accounts checked, including archived sites via Wayback Machine

KEY FEATURES:
=============

1. **Profile Image Extraction** - Automatically downloads Instagram profile pictures when found
2. **Comprehensive PDF Reports** - Generates detailed PDF reports with all found accounts and clickable links
3. **30+ Social Networks** - Checks major platforms plus archived sites via Wayback Machine
4. **Smart Detection** - Properly handles non-existent profiles and error pages
5. **Progress Indicators** - Visual progress dots and color-coded output
6. **Rate Limiting** - Randomized pausing between lookups to avoid getting blocked
7. **User Agent Rotation** - Uses +8500 different User Agent strings (can override via -u arg)
8. **Proxy Support** - Tor and HTTP proxy support via -p arg
9. **SSL Error Handling** - Automatically handles sites with certificate issues
10. **Modern Python** - Built for Python 3.12+ with modern syntax and best practices

INSTALLATION:
=============

**Using uv (recommended - fastest):**

First install uv::

    curl -LsSf https://astral.sh/uv/install.sh | sh

Then install spry::

    uv pip install spry

**Using pip:**

::

    pip install spry

**From source:**

::

    git clone git@github.com:james-see/spry.git
    cd spry
    uv sync
    uv run spry [username]

or::

    uv run python spry-run.py [username]

DEV PATH?

the goal is to get to +100 services that have public url user name profile links to check and gather information from

EXAMPLES:
=========

Basic usage::

    spry jamesacampbell

Generate PDF report with all found accounts::

    spry jamesacampbell --report

Verbose mode (show user agent for each request)::

    spry jamesacampbell -v

Use with Tor proxy::

    spry jamesacampbell -p 127.0.0.1:9050

Set custom wait time between requests (1-10 seconds)::

    spry jamesacampbell -w 10

Override user agent::

    spry jamesacampbell -u "My Custom User Agent"

REQUIREMENTS:
=============

- Python 3.12 or higher
- uv (recommended) or pip for installation


