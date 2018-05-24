#!usr/bin/python2

import socket   #for network communication
import time	#for using time related function
import thread 	#for running two process simulteniously i.e. send and recv msg are independent on each other
import base64   #for encrytion of data

my_ip="127.0.0.1"
my_port = 8888

# AF_INET is for ipv4     SOCK_DGRAM  i.e UDP protocol defined by IEEE
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((my_ip,my_port))



def receive_msg():
	while 1:
		data = s.recvfrom(1000)	#dtat is type of tuple it has (msg,(ip,portNo))  here data[0] is msg  data[1] is (ip,portNo)
		print "\n\t\t\t\t\tmsg from client :  "+str(data[0])
def send_msg():
	while True:
		msg = raw_input("Enter msg : ")
		s.sendto(base64.b64encode(msg),("127.0.0.1",9999)) #this will send your msg "hii" it is msg ("ipaddress ",9999) is receiver ip and portNo
	

#calling both function using thread and both will call independently 
#the first argument is function name and second one is tuple where function argument will be transfer in form of tuple

thread.start_new_thread(send_msg,())
thread.start_new_thread(receive_msg,())

#after executing these two thread line when controler will come down then for stop the completion of program we are using pass which is like conteniue in c
while 1:
	pass
