#SPRY

social media intelligence from the command line

## OVERVIEW

WARNING:

this is in early beta

KEY FEATURES:

1. Saves profile images and content from each profile found in the directory that you ran the command from.
2. Puts all found data into a single PDF (username-report.pdf) in the directory that you ran the command from.
3. Progress DOTS and nice COLOURS assuming your terminal supports it.
4. Randomized pausing between lookups so you don't get blocked.
5. Randomized list of +8500 User Agent strings in use by default (can override via -u arg).
6. Proxy override via -p arg.
7. OVER 30 SOCIAL MEDIA ACCOUNT PROFILES AUTO-MAGICALLY CHECKED & SAVED

## EXAMPLES

_run via tor and check for username pooman_   
`spry pooman -p 127.0.0.1:9050`

_run without spitting out a PDF report at the end_
`spry pooman --no-report`

_run setting the random wait to be 1 to 10 seconds between calls_   
`spry pooman -w 10`

_run and print out extra info including the user agent used for each request_   
`spry pooman -v`

_run and override random user agent to specific one_   
`spry pooman -u MY COOL USERAGENT STRING NOT A BOT`
