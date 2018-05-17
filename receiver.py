#!usr/bin/python2

import socket

rec_ip = "192.168.43.8"
myport = 9999


# AF_INET is for ipv4     SOCK_DGRAM  i.e UDP protocol defined by IEEE
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# now connecting ip and port.... first argument is tuple
s.bind((rec_ip,myport))
 
#is deciding howmuch charecter receiver can receive maximumly  (buffer size)
while 1:
	s.recvfrom(1000)   #if 
