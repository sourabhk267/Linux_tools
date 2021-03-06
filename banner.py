#!/usr/bin/env python
import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    for port in range(1, 100):
        ip = "192.168.43.42"
        banner = retBanner(ip, port)
        if banner:
            cmd = "[+] {} : {}".format(ip, banner)
            print(cmd.encode())


main()