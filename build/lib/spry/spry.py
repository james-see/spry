#!/usr/bin/env python
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

from modules import core
import argparse

def main():
    parser = argparse.ArgumentParser(
        version=__version__,
        formatter_class=argparse.RawTextHelpFormatter,
        prog='spry',
        description=__description__,
        epilog = '''\
EXAMPLE:
check instagram
  spry jamesanthonycampbell
The ALIAS name is marked in yellow''')

    parser.add_argument('username', help='specific target domain, like domain.com')

    parser.add_argument('-w', help='specific path to wordlist file',
                        nargs=1, dest='wordlist', required=False)

    parser.add_argument('-r', '--resolve', help='resolve ip or domain name',
                        action='store_true', required=False)

    parser.add_argument('-z', '--zone', help='check for zone transfer',
                        action='store_true', required=False)

    args = parser.parse_args()
    # args strings
    username = args.username
    wlist = args.wordlist
    if wlist: wlist = wlist[0]

    # args True or False
    resolve = args.resolve
    zone = args.zone
    r=requests.get('https://www.instagram.com/jamesanthonycampbell')
    print(r)
    exit()
if __name__ == '__main__':
    main()
