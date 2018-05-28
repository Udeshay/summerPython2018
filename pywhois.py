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
	print query
	print server
	msg = s.recv(1000000000)
	print msg
	#return msg

#End of the perform_whois()
	


def get_whois_data(domain):

	#remove htttp and www
	#the replace() method will replace substring if exists with given sub string 
	#we are graping domain name from a given link
	domain = domain.replace('https://','')
	domain = domain.replace('http://','')
	domain = domain.replace('www.','')
	
	
	ext = domain.split('.')	#spliting complete domain name 
	print ext

	#if domain like .com .org .net etc
	if len(ext)<3 :  
		#if top level domain .com .org .net
		if (ext[-1] == 'com' or ext[-1] == 'org' or ext[-1] == 'net'):
			whois = 'whois.internic.net'
			domain_info = perform_whois(whois,domain)
	
		elif ext[-1] == 'edu':
			whois = 'whois.educause.net'
			domain_info = perform_whois(whois,domain)

		else :
			ext = domain.split('.')[-1]  #will give word after .
			
			if ext == 'in':
				#this server will tell about indian country domain		
				whois = 'whois.inregistry.net'   
				domain_info = perform_whois(whois , domain)
			else :
				# will tell about any country domain
				whois = 'whois.iana.org'   
				domain_info = perform_whois(whois , domain)
	else :
		if ext == 'in':
				#this server will tell about indian country domain		
				whois = 'whois.inregistry.net'  
				domain_info = perform_whois(whois , domain)

	#returning the reply
	return domain_info












domain_name = (sys.argv[1])  #will take domin_name from command line argument  ...sys.argv[1] taking only one input as a string 

print get_whois_data(domain_name)
































