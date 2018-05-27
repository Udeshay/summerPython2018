#!/usr/bin/python

'''
program to fetch domain name information
'''

import socket , sys


def perform_whois(server,query) :
	#socket connection
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	s.connect((server , 43))
	s.send(query + '\r\n')
	
	msg = s.recv(10000)
	return msg

#End of the perform_whois()
	


def get_whois_data(domain):

	#remove htttp and www
	#the replace() method will replace substring if exists with given sub string 
	#we are graping domain name from a given link
	domain = domain.replace('https://','')
	domain = domain.replace('http://','')
	domain = domain.replace('www.','')
	
	#print domain
	#get the extension , .com , .org , .edu
	ext = domain[-3:]
	print ext

	#if top level domain .com .org .net
	if (ext == 'com' or ext == 'org' or ext == 'net'):
		whois = 'whois.internic.net'
		domain_info = perform_whois(whois,domain)

	else :
		ext = domain.split('.')[-1]  #will give word after .

		#this server will tell about perticuler country		
		whois =  'whois.inregistry.net'  #'whois.iana.org'
		domain_info = perform_whois(whois , domain)

	#returning the reply
	return domain_info












domain_name = sys.argv[1]  #will take domin_name from command line argument  ...sys.argv[1] taking only one input as a string 
print get_whois_data(domain_name)
































