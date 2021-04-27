
import requests
import webbrowser
import pyscreenshot
from datetime import datetime
import time
import argparse
from expressvpn import connect_alias
from expressvpn import disconnect

print("""_-====-__-======-__-========-_____-============-__
               _(                                                 _)
            OO(           _/_ _  _  _/_   _/_ _  _  _/_           )_
           0  (_          (__(_)(_) (__   (__(_)(_) (__            _)
         o0     (_                                                _)
        o         '=-___-===-_____-========-___________-===-dwb-='
      .o                                _________
     . ______          ______________  |         |      _____
   _()_||__|| ________ |            |  |_________|   __||___||__
  (         | |      | |            | __Y______00_| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"=P
#####################################################################
""")

parser = argparse.ArgumentParser()
requiredArguments = parser.add_argument_group("Required arguments")
requiredArguments.add_argument("--keyword", "-k", help="set keyword to look for in the URL source code", type=str)
requiredArguments.add_argument("--width", "-w", help="set output width", type=int)
requiredArguments.add_argument("--height", "-hg", help="set output height", type=int)
requiredArguments.add_argument("--url", "-u", help="set target URL", type=str)
requiredArguments.add_argument("--exuser", "-exu", help="set ExpressVPN username", type=str)
requiredArguments.add_argument("--expass", "-exp", help="set ExpressVPN password", type=str)

args = parser.parse_args()

if args.url:
    url = "%s" % args.url
elif args.keyword:
    keyword = "%s" % args.keyword
elif args.width:
    screen_width = "%i" % args.width
elif args.height:
    screen_height = "%i" % args.height
elif args.exuser:
    expressvpn_user = "%s" % args.exuser
elif args.expass:
    expressvpn_password = "%s" % args.expass
else:
    print("Invalid argument. Use --help or -h to see the valid options")
    exit(2)

current_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
screenshot_extension = ".png"
status = requests.get(args.url).status_code
expressvpn_list = ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech\ Republic", "Denmark", "Spain", "Estonia", "Finland", "France", "Germany", "Greece", "Hong\ Kong", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Serbia", "Slovakia", "Switzerland", "Sweden", "United\ Kingdom", "United\ States"]


class Colors:
    OK_CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    Color_Off = "\033[0m"


def url_check():
    if status == 404:
        print(url, "is not up, returned ", status)
    elif status == 200:
        print(url, "is up, returned ", status)
        source_code = requests.get(url).text
        if args.keyword in source_code:
            print(Colors.OK_CYAN + url, "is a match!")
            webbrowser.open(url)
            print("Taking screenshot..." + Colors.Color_Off)
            time.sleep(7)
        else:
            print(Colors.RED + url, "is not a match." + Colors.Color_Off)

    elif status == 301 or 302:
        print(Colors.YELLOW + url, "is a redirecting URL." + Colors.Color_Off)
    else:
        print(url, "returned ", status)


for country in expressvpn_list:
    connect_alias(country)
    url_check()
    screenshot = pyscreenshot.grab(bbox=(0, 35, args.width, args.height))
    screenshot.save(country + screenshot_extension)
    time.sleep(3)
    disconnect()



