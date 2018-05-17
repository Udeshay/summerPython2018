#!usr/bin/python2

import socket


# AF_INET is for ipv4     SOCK_DGRAM  i.e UDP protocol defined by IEEE
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# argument is as tuple second one ..ipaddress and port address of receiver
s.sendto("hiii",("10.42.0.1",9999))    #this will send your 
