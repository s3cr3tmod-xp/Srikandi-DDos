# -*- coding: utf-8 -*-  
#! /usr/bin/python3.11 -sP
import os
import requests
import datetime
import asyncio
import validators
from urllib.parse import urlparse
from sys import stdout
from colorama import Fore, Style, init
import logging 
import time
# Inisialisasi Colorama dan Logging  
init(autoreset=True)
# Pengaturan Logging yang benar
logging.basicConfig(
    filename='attack.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  # Perbaiki dari levellevel menjadi levelname 
  datefmt='%Y-%m-%d %H:%M:%S'
)

# Fungsi untuk Logging Informasi Serangan
def log_attack_status(message, level='info', print_to_terminal=True):
    if level == 'info':
        my_regex = r"\Afoo"
        logging.info(message)
        if print_to_terminal:
            print(f"{Fore.CYAN}|    [INFO] {message.ljust(63)}|")
    elif level == 'error':
        logging.error(message)
        if print_to_terminal:
            print(f"{Fore.RED}|    [ERROR] {message.ljust(63)}|")
    elif level == 'warning':
        logging.warning(message)
        if print_to_terminal:
            print(f"{Fore.YELLOW}|    [WARNING] {message.ljust(63)}|")
      

# Fungsi untuk Menampilkan Header HUDAIRUL-AQSHA dengan Warna
def display_header():
    header_lines = [
    f"{Fore.BLUE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
    f"{Fore.BLUE}▒▒██████╗▒██████╗▒▒██╗▒██╗▒▒▒██╗▒▒▒████╗▒▒▒████╗▒▒▒██╗▒██████╗▒▒▒██╗▒▒",
    f"{Fore.BLUE}▒▒██╔═══╝▒██╔══██╗▒██║▒██║▒▒██╔╝▒▒██╔═██╗▒▒██╔██╚╗▒██║▒██║▒▒▒██║▒██║▒▒ ",
    f"{Fore.BLUE}▒▒██║▒▒▒▒▒██║▒▒██║▒██║▒██║▒██╔╝▒▒██║▒▒▒██║▒██║▒██╚╗██║▒██║▒▒▒██║▒██║▒▒ ",
    f"{Fore.BLUE}▒▒██████╗▒██║▒▒██║▒██║▒██║██╔╝▒▒▒██║▒▒▒██║▒██║▒▒██╚██║▒██║▒▒▒██║▒██║▒▒ ",
    f"{Fore.BLUE}▒▒╚═══██║▒██████╚╗▒██║▒██║▒██╚╗▒▒██║█████║▒██║▒▒▒████║▒██║▒▒▒██║▒██║▒▒ ",
    f"{Fore.BLUE}▒▒██████║▒██╔══██║▒██║▒██║▒▒██╚╗▒██║▒▒▒██║▒██║▒▒▒▒███║▒██████╔╝▒▒██║▒▒ ",
    f"{Fore.BLUE}▒▒╚═════╝▒╚═╝▒▒╚═╝▒╚═╝▒╚═╝▒▒▒╚═╝▒╚═╝▒▒▒╚═╝▒╚═╝▒▒▒▒╚══╝▒╚═════╝╝▒▒╚═╝▒▒ ",
    f"{Fore.BLUE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
    ]

    # Tampilkan header dengan warna
    for line in header_lines:
        print(line)
      
    # Versi dan URL
    print(f"{Fore.BLUE}╔{'═' * 68}╗")
    print(f"{Fore.BLUE}║\033[48;5;4m{' ' * 27}\033[38;5;206mAuthor: KunFz{' ' * 27} {Fore.BLUE}\033[0m║")
    print(f"{Fore.BLUE}║\033[48;5;4m{' ' * 25}\033[38;5;206mAdm: Z'black 313{' ' * 26} {Fore.BLUE}\033[0m║")
    print(f"{Fore.BLUE}║\033[48;5;4m{' ' * 20}\033[38;5;206mCan be used but not shared{' ' * 21} {Fore.BLUE}\033[0m║")
    print(f"{Fore.BLUE}╚{'═' * 68}╝")

# Fungsi untuk Meminta Input dari Pengguna dengan Tampilan Rapi
def get_user_input(prompt_message):
    
    print(f"{Fore.WHITE}║[?] {prompt_message}")
    return input(f"{Fore.BLUE}┗━━━> ").strip()

# Fungsi Countdown untuk Menampilkan Waktu Serangan
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        remaining_time = (until - datetime.datetime.now()).total_seconds()
        if remaining_time > 1:
            time.sleep(1),
            stdout.flush()
            stdout.write(f"\r\033[48;5;7m\033[30m+Target-Url\033[0m* \033[38;5;39m{target_url} \033[38;5;111mRemaining_time: \033[37m{remaining_time:.2f}") 
            print(f"\033[38;5;154m-Target-Url* \033[38;5;206m {target_url} \033[32mRemaining_time: \033[38;5;37m{remaining_time:.2f}")
        else:
            stdout.flush()
            stdout.write(f"\r{Fore.RED}|  [*]  {Fore.YELLOW}חודאירול אקשה    {Fore.CYAN}התקפה נעשתה!{' ' * 53}|\n")
            print(f"{Fore.CYAN}|{'=' * 74}|")
            return

# Validasi URL dan Parsing Target
def get_target(url):
    if not validators.url(url):
        log_attack_status(f"URL tidak valid: {url}", level='error')
        raise ValueError(f"URL tidak valid: {url}")

    target = {
        'uri': urlparse(url).path or "/",
        'host': urlparse(url).netloc,
        'scheme': urlparse(url).scheme,
        'port': urlparse(url).netloc.split(":")[1] if ":" in urlparse(url).netloc else ("443" if urlparse(url).scheme == "https" else "80")
    }
    log_attack_status(f"Target diperoleh: {target['host']} ({target['scheme']}://{target['host']}:{target['port']}{target['uri']})")
    return target

# Fungsi Serangan Utama
def launch_attack(target_url, duration):
    target = get_target(target_url)

    # Inisialisasi Serangan dan Waktu Serangan
    log_attack_status(f"Meluncurkan serangan ke {target['host']} untuk {duration} detik...")
    countdown(duration)

if __name__ == "__main__":
    # Tampilkan Header
    display_header()

    # Prompt untuk input dari pengguna dengan tampilan yang rapi
    attemps = 0
    while attemps < 100:
       print("\033[38;5;39m┏━━━━━━━⬣")
       username = input("\033[38;5;39m┗> Enter your username: \033[32m")
       print("\033[38;5;39m┏━━━━━━━⬣")
       password = input("\033[38;5;39m┗> Enter your password: \033[32m")
       print("\033[104m\033[0m")
       if username == 'srk313' and password == 'srk313':
           print("\033[7m•••>       SRIKANDI BLACK ARMY\033[0m")
           print(f"{Fore.BLUE}┏━━━━━━━⬣")
           break
       else:
           print('Incorrect credentials. Check if you have Caps lock on and try again.')
           attemps += 1
           continue
      
    target_url = get_user_input("Enter the target url:   ")
    while not validators.url(target_url):
        print(f"{Fore.RED}|[ERROR] URL tidak valid. Coba lagi.{' ' * 37}|")
        print(f"{Fore.CYAN}|{'=' * 74}|")
        target_url = get_user_input("  Server URL:")

    try:
        attack_duration = int(get_user_input("Enter the duration (second):"))
    except ValueError:
        attack_duration = 60  # Default durasi

    # Luncurkan serangan
    launch_attack(target_url, attack_duration)
