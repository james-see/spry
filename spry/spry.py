# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.3.1"
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

import argparse, requests

def main():
    parser = argparse.ArgumentParser(
        #version='0.1.7',
        formatter_class=argparse.RawTextHelpFormatter,
        prog='spry',
        description='social media scanner',
        epilog = '''EXAMPLE: \n check instagram \n spry jamesanthonycampbell \n The ALIAS name is marked in yellow''')

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
    r=requests.get('https://www.instagram.com/'+username)
    #print(r.text)
    print("Status code for instagram for that user is: {}".format(r.status_code))

