#!usr/bin/python2

import socket

rec_ip = "127.0.0.1"
myport = 9999


# AF_INET is for ipv4     SOCK_DGRAM  i.e UDP protocol defined by IEEE
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# now connecting ip and port.... first argument is tuple
s.bind((rec_ip,myport))
 
#is deciding howmuch charecter receiver can receive maximumly  (buffer size)
while 1:
	data = s.recvfrom(1000)	#dtat is type of tuple it has (msg,(ip,portNo))  here data[0] is msg  data[1] is (ip,portNo)
	print "msg from client :  "+str(data[0])
	rply = raw_input("Pleae Enter reply : ")
	s.sendto(rply,data[1])
		
	  
