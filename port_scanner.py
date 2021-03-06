#!/usr/bin/env python

# there are nearly 65k ports.
from socket import *
import optparse
from termcolor import colored
from threading import *


def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print('[+] %d/tcp Open' % tgtPort)
    except:
        print('[-] %d/tcp Closed' %tgtPort)
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts):
    global tgtIP
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Unknown Host %s ' %tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan Result For: " + tgtName[0])
    except:
        print("[+] Scan Result for: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
def main():
    parser = optparse.OptionParser("Usage of program: " + "-h <target host> -p <target ports>")
    parser.add_option('-h', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPost', type='string', help='specify target posts seperated by comma')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPosts = str(options.tgtPost).split(',')
    if (tgtHost == None) | (tgtPosts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPosts)

if __name__ == '__main__':
    main()


