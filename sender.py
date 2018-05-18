#!usr/bin/python2

import socket
import time


# AF_INET is for ipv4     SOCK_DGRAM  i.e UDP protocol defined by IEEE
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# argument is as tuple second one ..ipaddress and port address of receiver



while True:
	msg = raw_input("Enter msg : ")
	s.sendto(msg,("127.0.0.1",9999)) #this will send your msg "hii" it is msg ("ipaddress ",9999) is receiver ip and portNo
	time.sleep(1)
	print s.recvfrom(1000)  #1000 is limit hw much maximum character this will except
    
