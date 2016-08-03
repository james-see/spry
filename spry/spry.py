# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.3.9"
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
import sys
from time import sleep
import argparse, requests
from random import random, randint
from clint.textui import progress
try:
    from modules import stuff
    from modules import core
except:
    from spry.modules import stuff
    from spry.modules import core

def main():
    parser = argparse.ArgumentParser(
        #version='0.1.7',
        formatter_class=argparse.RawTextHelpFormatter,
        prog='spry',
        description='social media scanner',
        epilog = '''EXAMPLE: \n check instagram \n spry jamesanthonycampbell \n The ALIAS name is marked in yellow''')

    parser.add_argument('username', help='specific target domain, like domain.com')

    parser.add_argument('-p', '--proxy', help='proxy in the form of 127.0.0.1:8118',
                        nargs=1, dest='setproxy', required=False)

    parser.add_argument('-w', '--wait', help='max random wait time in seconds, 5 second default',
                        dest='setwait', nargs='?',const=3,type=int,default=3)

    args = parser.parse_args()
    # args strings
    username = args.username
    setproxy = args.setproxy
    setwait = args.setwait
    i = 0

    social_networks_list=['https://www.instagram.com/','https://foursquare.com/']
    print('Starting to process list of social networks now...\n')
    for soc in social_networks_list:
        print("{} loading".format(soc))
        sleep(randint(3,setwait))
        r=requests.get(soc+username,stream=True)
        try:
            total_length = int(r.headers.get('content-length'))
        except:
            total_length = 1024
        for chunk in progress.mill(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            sleep(random() * 0.2)
            if chunk:
                #sys.stdout.write(str(chunk))
                sys.stdout.flush()
    #print(r.text)
        if r.status_code == 200:
            print("user found")
            i = i+1
        else:
            print("Status code: {} no user found".format(r.status_code))
    print('Total networks with username found: {}'.format(i))
class Boo(stuff.Stuff):
    pass

if __name__ == '__main__':
    main()
