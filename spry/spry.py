# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.4.1"
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
from bs4 import BeautifulSoup, SoupStrainer
try:
    from modules import stuff
    from modules import core
    from modules.pdf_maker import *
except:
    from spry.modules import stuff
    from spry.modules import core
    from spry.modules.pdf_maker import *


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

    parser.add_argument('-w', '--wait', help='max random wait time in seconds, 5 second default (randomly wait 1-5 seconds)',
                        dest='setwait', nargs='?',const=3,type=int,default=3)

    parser.add_argument('--report', dest='reporting', action='store_true',help='save PDF report or not, default TRUE, saved as username.pdf')
    parser.add_argument('--no-report', dest='reporting', action='store_false')
    parser.set_defaults(reporting=True)

    args = parser.parse_args()
    # args strings
    username = args.username
    setproxy = args.setproxy
    setwait = args.setwait
    reporting = args.reporting
    i = 0

    social_networks_list=['https://www.instagram.com/','https://foursquare.com/','https://www.flickr.com/photos/']
    totalnetworks = len(social_networks_list) # get the total networks to check
    print('Starting to process list of {} social networks now...\n\n'.format(totalnetworks))
    for soc in social_networks_list:
        print("{} loading".format(soc))
        sleep(randint(1,setwait))
        sys.stdout.flush()
        r=requests.get(soc+username,stream=True)
        if soc == 'https://www.instagram.com/':
            #print(r.text)
            soup = BeautifulSoup(r.content,'html.parser')
            aa = soup.find("meta", {"property":"og:image"})
            print (aa['content']) # this is the instagram profile image
            instagram_profile_img = requests.get(aa['content'])
            open('./'+username+'.jpg' , 'wb').write(instagram_profile_img.content)
            #exit()
        try:
            total_length = int(r.headers.get('content-length'))
        except:
            total_length = 1024
        for chunk in progress.mill(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            sleep(random() * 0.2)
            if chunk:
                #sys.stdout.write(str(chunk))
                sys.stdout.flush()
        sys.stdout.flush()
    #print(r.text)
        if r.status_code == 200:
            print("user found")
            i = i+1
        else:
            print("Status code: {} no user found".format(r.status_code))
    print('Total networks with username found: {}'.format(i))
    if reporting: # if pdf reporting is turned on (default on)
        create_pdf(username)
class Boo(stuff.Stuff):
    pass

if __name__ == '__main__':
    main()
