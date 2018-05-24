#!usr/bin/python2

import socket
import thread	#fro running two task independently
import base64

rec_ip = "127.0.0.1"
myport = 9999


# AF_INET is for ipv4     SOCK_DGRAM  i.e UDP protocol defined by IEEE
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# now connecting ip and port.... first argument is tuple
s.bind((rec_ip,myport))
 

def receive_msg():
	while 1:
		data = s.recvfrom(1000)	#dtat is type of tuple it has (msg,(ip,portNo))  here data[0] is msg  data[1] is (ip,portNo)
		print "\n\t\t\t\t\tmsg from client :  "+ base64.b64decode(str(data[0]))
	
def send_msg():
	while 1:
		rply = raw_input("Pleae Enter reply : ")
		s.sendto(rply,("127.0.0.1",8888))

#calling both function using thread and both will call independently 
#the first argument is function name and second one is tuple where function argument will be transfer in form of tuple
thread.start_new_thread(receive_msg,())
thread.start_new_thread(send_msg,())

#after executing these two thread line when controler will come down then for stop the completion of program we are using pass which is like conteniue in c
while 1:
	pass
		
	  
