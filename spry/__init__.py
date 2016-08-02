import os
_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data(path):
    return os.path.join(_ROOT, 'wordlist', path)
__version__ = '0.1.5'
__title__ = 'spry'
__author__ = 'James Campbell'
__description__ = 'social media scanner'
__email__ = 'james@jamescampbell.us'
__license__ = 'GPLv3'
__copyright__ = 'Copyright 2016 James Campbell'
