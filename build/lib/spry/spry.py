# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.5.2"
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
cur_version = sys.version_info
from time import sleep
import argparse, requests
from random import random, randint
import random
from clint.textui import progress # for the dots!
from bs4 import BeautifulSoup, SoupStrainer # parse the html!
try: from urllib.parse import urlparse # get domain names!
except:
    from urlparse import urlparse
    cur_version = 2.7
    #sys.path.append(PYTHONPATH)
from termcolor import *

if cur_version < 3:
    try:
        from .modules import stuff
        from .modules import core
        from .modules.pdf_maker import *
        from .modules.useragents import *
    except:
        from modules import stuff
        from modules import core
        from modules.pdf_maker import *
        from modules.useragents import *
        #exit('your python version is too old, please install python 3+ to get SPRY to work')
else:
    try:
        from modules import stuff
        from modules import core
        from modules.pdf_maker import *
        from modules.useragents import *
    except:
        from spry.modules import stuff
        from spry.modules import core
        from spry.modules.pdf_maker import *
        from spry.modules.useragents import *


welcomer = '\n++++++++++++++++++++++++++++\n+++ SPRY +++ WELCOME +++++++\n+++ s0c1@l m3d1a sc@nn3r +++\n++++++++++++++++++++++++++++\n'
usingtor = False
def main():
    # welcome to the danger zone

    parser = argparse.ArgumentParser(
        # random comment here for no reason ;)
        formatter_class=argparse.RawTextHelpFormatter,
        prog='spry',
        description='++++++++++++++++++++++++++++\n+++ SPRY +++++++++++++++++++\n+++ s0c1@l m3d1a sc@nn3r +++\n++++++++++++++++++++++++++++',
        epilog = '''EXAMPLE: \n check instagram \n spry jamesanthonycampbell \n ''')

    parser.add_argument('username', help='specific username, like realdonaldtrump')

    parser.add_argument('-p', '--proxy', help='proxy in the form of 127.0.0.1:8118',
                        nargs=1, dest='setproxy', required=False)

    parser.add_argument('-w', '--wait', help='max random wait time in seconds, \n5 second default (randomly wait 1-5 seconds)',
                        dest='setwait', nargs='?',const=3,type=int,default=3)
    parser.add_argument('-u', '--user-agent', help='override random user-agent\n(by default randomly selects between \n+8500 different user agent strings',
                        dest='useragent', nargs='?',const='u',default='u')
    parser.add_argument('--no-report', dest='reporting', action='store_false')
    parser.add_argument('-v','--verbose-useragent',dest='vu',action='store_true')
    parser.add_argument('--version', action='version',
                    version='%(prog)s {version}'.format(version='Version: '+__version__))
    parser.set_defaults(reporting=True,vu=False)
    args = parser.parse_args()
    cprint(welcomer,'red')
    # args strings
    username = args.username
    setproxy = args.setproxy
    # note, the correct way to check if variable is NoneType
    if setproxy != '' and setproxy is not None:
        proxyoverride = True
        if '9050' in setproxy[0] or '9150' in setproxy[0]:
            usingtor = True
        else:
            usingtor = False
    else:
        proxyoverride = False
    setwait = args.setwait
    reporting = args.reporting
    useragent = args.useragent
    vu = args.vu
    if useragent == 'u':
        overrideuseragent = False
        useragent = random.choice(useragents) # if user agent override not set, select random from list
    if vu:
        cprint('\nUseragent set as %s\n' % (useragent,),'blue')
    headers = {'User-Agent': useragent}
    i = 0 # counter for how many are 200's
    social_networks_list=['https://twitter.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://foursquare.com/','https://www.flickr.com/photos/','https://www.facebook.com/','https://www.reddit.com/user/','https://new.vk.com/','https://github.com/','https://ok.ru/','https://www.twitch.tv/','https://venmo.com/','http://www.goodreads.com/','http://www.last.fm/user/','https://api.spotify.com/v1/users/','https://www.pinterest.com/','https://keybase.io/','https://bitbucket.org/','https://pinboard.in/u:','https://disqus.com/by/','https://badoo.com/profile/','http://steamcommunity.com/id/','http://us.viadeo.com/en/profile/','https://www.periscope.tv/','https://www.researchgate.net/profile/','https://www.etsy.com/people/','https://myspace.com/','http://del.icio.us/','https://my.mail.ru/community/','https://www.xing.com/profile/']
    totalnetworks = len(social_networks_list) # get the total networks to check
    print('\n\n[*] Starting to process list of {} social networks now [*]\n\n'.format(totalnetworks))
    for soc in social_networks_list:
        # get domain name
        domainname = urlparse(soc).netloc
        domainnamelist = domainname.split('.')
        for domainer in domainnamelist:
            if len(domainer) > 3 and domainer != 'vk' and domainer != 'ok' and domainer != 'last' and domainer != 'mail':
                realdomain = domainer
            elif domainer == 'vk':
                realdomain = domainer
            elif domainer == 'ok':
                realdomain = domainer+'.ru'
            elif domainer == 'last':
                realdomain = domainer+'.fm'
            elif domainer == 'mail':
                realdomain = domainer+'.ru'
        # get proxy settings if any
        if proxyoverride == True:
            if usingtor:
                socks_proxy = "socks5://"+setproxy[0]
                proxyDict = { "http" : socks_proxy }
            else:
            #print(setproxy)
                http_proxy  = "http://"+setproxy[0]
                https_proxy = "https://"+setproxy[0]
                proxyDict = {
                              "http"  : http_proxy,
                              "https" : https_proxy
                            }
        sleep(randint(1,setwait))
        sys.stdout.flush()
        # try to load the social network for the respective user name
        # make sure to load proxy if proxy set otherwise don't pass a proxy arg
        if proxyoverride == True:
            r=requests.get(soc+username,stream=True, headers=headers, proxies=proxyDict)
        else:
            r=requests.get(soc+username,stream=True, headers=headers)
        # switch user agents again my friend
        if overrideuseragent == False:
            useragent = random.choice(useragents)
            # if user agent override not set, select random from list
        if vu: # if verbose output then print the user agent string
            cprint('\nUseragent set as %s\n' % (useragent,),'blue')
        if soc == 'https://www.instagram.com/' and r.status_code == 200:
            #print(r.text)
            soup = BeautifulSoup(r.content,'html.parser')
            aa = soup.find("meta", {"property":"og:image"})
            # test instagram profile image print
            #print (aa['content']) # this is the instagram profile image
            instagram_profile_img = requests.get(aa['content']) # get instagram profile pic
            open('./'+username+'.jpg' , 'wb').write(instagram_profile_img.content)
            #exit()
        try:
            total_length = int(r.headers.get('content-length'))
        except:
            total_length = 102399
        for chunk in progress.dots(r.iter_content(chunk_size=1024),label='Loading '+realdomain):
            sleep(random.random() * 0.2)
            if chunk:
                #sys.stdout.write(str(chunk))
                sys.stdout.flush()
        sys.stdout.flush()
    #print(r.text)
        if r.status_code == 200:
            cprint("user found",'green')
            i = i+1
        else:
            cprint("Status code: {} no user found".format(r.status_code),'red')
    print('\n\n[*] Total networks with username found: {} [*]\n'.format(i))
    if reporting: # if pdf reporting is turned on (default on)
        create_pdf(username)
        cprint('Report saved as {}-report.pdf. \nTo turn off this feature use the --no-report flag.\n'.format(username),'yellow')
class Boo(stuff.Stuff):
    pass

if __name__ == '__main__':
    main()
