import os
import time
import threading
from random import randint
from colorama import Fore, init

init(autoreset=True)

stop_loop = False

def vcolor(line):
    return line

logo = """
  _____ _____        _____                           _             
 |_   _|  __ \      / ____|                         | |            
   | | | |__) |__  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   | | |  ___/ __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  _| |_| |   \__ \ | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_____|_|   |___/  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
 
\t\tTelegram Channel Link : t.me/Ev3l_m0rty_Channel / Telegram Admin Link: t.me/Ev3l_m0rty
"""

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
os.system(["clear", "cls"][os.name == 'nt'])
for line in logo.splitlines():
    print("".join(colors[randint(0, len(colors) - 1)] + vcolor(line)))
    time.sleep(0.05)

def dip_ipgen():
    while not stop_loop:
        a = randint(0, 255)
        b = randint(0, 255)
        c = randint(0, 255)
        d = randint(0, 255)
        evilmr = '{}.{}.{}.{}'.format(a, b, c, d)
        print(Fore.WHITE + "\t\t[" + Fore.BLUE + "+" + Fore.WHITE + "] Generated IP : " + Fore.RED + '| ' + Fore.GREEN + evilmr + Fore.RED + " | ")
        with open('Generated_IPs.txt', 'a') as file:
            file.write(evilmr + '\n')
        time.sleep(0.01)

def key_listener():
    input("Press Enter to stop generating IPs...")
    global stop_loop
    stop_loop = True

# Create and start threads
thread_generation = threading.Thread(target=dip_ipgen)
thread_input = threading.Thread(target=key_listener)

thread_generation.start()
thread_input.start()

thread_generation.join()
thread_input.join()
