#!/usr/bin/python

import socket
import sys
import errno

print "I will scan all ports at " + str(sys.argv[1])
host = sys.argv[1]
port = 0


while port < 65535:
    port += 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pair = (host, port)
    error = s.connect_ex(pair)
    s.close()
    print '%s\r' % str(port),
    if error == 0:
        print "Success at port: " + str(port)


