"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.5.7"
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
import argparse
import requests
from random import random, randint
import random
from clint.textui import progress  # for the dots!
from bs4 import BeautifulSoup, SoupStrainer  # parse the html!
from urllib.parse import urlparse  # get domain names!
from termcolor import *
import urllib3

# Suppress SSL warnings for sites with certificate issues
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    parser.add_argument('--report', dest='reporting', action='store_true')
    parser.add_argument('-v','--verbose-useragent',dest='vu',action='store_true')
    parser.add_argument('--version', action='version',
                    version=f'%(prog)s Version: {__version__}')
    parser.set_defaults(reporting=False,vu=False)
    args = parser.parse_args()
    cprint(welcomer,'red')
    # args strings
    username = args.username
    setproxy = args.setproxy
    # note, the correct way to check if variable is NoneType
    if setproxy != '' and setproxy is not None:
        proxyoverride = True
        if '9050' in setproxy[0] or '9150' or 'tor' in setproxy[0]:
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
        cprint(f'\nUseragent set as {useragent}\n', 'blue')
    headers = {'User-Agent': useragent}
    i = 0 # counter for how many are 200's
    found_accounts = []  # List to store found account URLs
    social_networks_list=[
        'https://x.com/',  # Twitter is now x.com
        'https://www.instagram.com/',
        'https://www.linkedin.com/in/',
        'https://foursquare.com/',
        'https://www.flickr.com/photos/',
        'https://www.facebook.com/',
        'https://www.reddit.com/user/',
        'https://new.vk.com/',
        'https://github.com/',
        'https://ok.ru/',
        'https://www.twitch.tv/',
        'https://venmo.com/',
        'http://www.goodreads.com/',
        'http://www.last.fm/user/',
        'https://api.spotify.com/v1/users/',
        'https://www.pinterest.com/',
        'https://keybase.io/',
        'https://bitbucket.org/',
        'https://pinboard.in/u:',
        'https://disqus.com/by/',
        'https://badoo.com/profile/',
        'http://steamcommunity.com/id/',
        'https://www.periscope.tv/',
        'https://www.researchgate.net/profile/',
        'https://www.etsy.com/people/',
        'https://my.mail.ru/community/',
        'https://www.xing.com/profile/',
        # Dead/broken sites - using Wayback Machine (format: web.archive.org/web/TIMESTAMP/ORIGINAL_URL)
        # Using 20200101000000 as timestamp to get a snapshot from around 2020
        'https://web.archive.org/web/20200101000000/https://myspace.com/',
        'https://web.archive.org/web/20200101000000/http://del.icio.us/',
        'https://web.archive.org/web/20200101000000/http://us.viadeo.com/en/profile/',
    ]
    totalnetworks = len(social_networks_list) # get the total networks to check
    print(f'\n\n[*] Starting to process list of {totalnetworks} social networks now [*]\n\n')
    for soc in social_networks_list:
        # get domain name
        domainname = urlparse(soc).netloc
        
        # Handle Wayback Machine URLs - extract the original domain
        if 'web.archive.org' in domainname:
            # Extract original URL from Wayback Machine URL
            # Format: web.archive.org/web/TIMESTAMP/ORIGINAL_URL
            parts = soc.split('/')
            if len(parts) > 5:
                original_url = '/'.join(parts[5:])
                domainname = urlparse(original_url).netloc
        
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
        # DONT FORGET TO HANDLE LOAD TIMEOUT ERRORS! - ADDED exception handlers finally 2-5-2017 JC
        request_timeout = 30  # 30 second timeout
        is_instagram = soc == 'https://www.instagram.com/'
        
        # Handle Wayback Machine URLs specially
        is_wayback = 'web.archive.org' in soc
        verify_ssl = not is_wayback  # Wayback Machine and some old sites have SSL issues
        
        if proxyoverride == True:
            try:
                r = requests.get(soc+username, stream=True, headers=headers, proxies=proxyDict, timeout=request_timeout, verify=verify_ssl)
            except requests.Timeout as err:
                print(err)
                continue
            except requests.exceptions.SSLError:
                # Retry without SSL verification for sites with certificate issues
                try:
                    r = requests.get(soc+username, stream=True, headers=headers, proxies=proxyDict, timeout=request_timeout, verify=False)
                except requests.RequestException as err:
                    print(err)
                    continue
            except requests.RequestException as err:
                print(err)
                continue
        else:
            try:
                r = requests.get(soc+username, stream=True, headers=headers, timeout=request_timeout, verify=verify_ssl)
            except requests.Timeout as err:
                print(err)
                continue
            except requests.exceptions.SSLError:
                # Retry without SSL verification for sites with certificate issues
                try:
                    r = requests.get(soc+username, stream=True, headers=headers, timeout=request_timeout, verify=False)
                except requests.RequestException as err:
                    print(err)
                    continue
            except requests.RequestException as err:
                print(err)
                continue
        # switch user agents again my friend
        if overrideuseragent == False:
            useragent = random.choice(useragents)
            # if user agent override not set, select random from list
        if vu:  # if verbose output then print the user agent string
            cprint(f'\nUseragent set as {useragent}\n', 'blue')
        
        # For Instagram, we need to read the content to parse it, so handle it specially
        is_instagram_error = False
        if is_instagram and r.status_code == 200:
            # Read content once for parsing
            content = r.content
            soup = BeautifulSoup(content, 'html.parser')
            
            # Check for og:image meta tag - non-existent profiles don't have it
            # This is the most reliable indicator since Instagram uses JS for error messages
            aa = soup.find("meta", {"property":"og:image"})
            
            if aa and 'content' in aa.attrs:
                image_url = aa['content']
                # Real Instagram profile images are from Instagram CDN
                # Check if it's a valid Instagram CDN URL
                if 'instagram.com' in image_url or 'cdninstagram.com' in image_url:
                    # Valid profile found - download the image
                    try:
                        instagram_profile_img = requests.get(image_url, timeout=request_timeout)
                        if instagram_profile_img.status_code == 200:
                            open(f'./{username}.jpg', 'wb').write(instagram_profile_img.content)
                    except requests.RequestException:
                        pass  # Skip if we can't download the image
                else:
                    # og:image exists but not from Instagram CDN - likely an error page
                    is_instagram_error = True
            else:
                # No og:image meta tag - this indicates a non-existent profile
                is_instagram_error = True
            
            # Backup check: look for error messages in page text (in case og:image check fails)
            if not is_instagram_error:
                page_text = soup.get_text().lower()
                is_instagram_error = any(error_text in page_text for error_text in [
                    "profile isn't available",
                    "sorry, this page isn't available",
                    "the link you followed may be broken",
                    "user not found"
                ])
            
            # Skip chunk iteration for Instagram since we already read the content
            print(f'Loading {realdomain}...', end='', flush=True)
            print(' done')
        else:
            # For other sites, show progress dots while streaming
            try:
                total_length = int(r.headers.get('content-length', 0))
            except (ValueError, TypeError):
                total_length = 0
            
            # Limit chunk processing to prevent infinite loops
            max_chunks = 10000  # Maximum number of chunks to process
            chunk_count = 0
            for chunk in progress.dots(r.iter_content(chunk_size=1024), label=f'Loading {realdomain}'):
                chunk_count += 1
                if chunk_count >= max_chunks:
                    break
                sleep(random.random() * 0.2)
                if chunk:
                    #sys.stdout.write(str(chunk))
                    sys.stdout.flush()
            sys.stdout.flush()
        #print(r.text)
        # For Instagram, we already checked for error pages above
        # Instagram returns 200 even for non-existent profiles, so we check content
        if r.status_code == 200 and not is_instagram_error:
            account_url = soc+username
            cprint(f"user found @ {account_url}", 'green')
            found_accounts.append(account_url)
            i = i+1
        else:
            if is_instagram_error:
                cprint(f"Status code: {r.status_code} no user found (Instagram error page)", 'red')
            else:
                cprint(f"Status code: {r.status_code} no user found", 'red')
    print(f'\n\n[*] Total networks with username found: {i} [*]\n')
    if reporting: # if pdf reporting is turned on (default on)
        create_pdf(username, i, found_accounts)
        cprint(f'Report saved as {username}-report.pdf. \nTo turn off this feature dont pass in the --report flag.\n', 'yellow')
class Boo(stuff.Stuff):
    pass

if __name__ == '__main__':
    main()
