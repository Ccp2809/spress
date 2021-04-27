# Spress.py
Script to automate the process of checking a URL with different ExpressVPN proxies and take screenshots of the content.

# Usage
'''
usage: spress.py [-h] [--keyword KEYWORD] [--width WIDTH] [--height HEIGHT] [--url URL] [--exuser EXUSER]
                 [--expass EXPASS]

optional arguments:
  -h, --help            show this help message and exit

Required arguments:
  --keyword KEYWORD, -k KEYWORD
                        set keyword to look for in the URL source code
  --width WIDTH, -w WIDTH
                        set output width
  --height HEIGHT, -hg HEIGHT
                        set output height
  --url URL, -u URL     set target URL
  --exuser EXUSER, -exu EXUSER
                        set ExpressVPN username
  --expass EXPASS, -exp EXPASS
                        set ExpressVPN password
'''

# requirements.txt
'''
requests
webbrowser
expressvpn
pyscreenshot
'''
