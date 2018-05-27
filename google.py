#!user/etc/python

import time     #for time function like sleep() etc
import webbrowser  #for accessing webbrowser from programe
import datetime	   #for fetching current time and date
from bs4 import BeautifulSoup  #for scraping data from web page
import requests  #for sending requesting for a specific url on browser but without opening that
import os  #for running commands on terminal
import commands   #for execute command on linux terminal




#main menu to show user
def google_search_menu():
	option = '''
	press 1: to enter anything- split each word and search on google
	press 2: enter website to find all URL of that page
	press 3: enter anything to find image answer
	press 4: current time and date
	press 5: open default browser
	press 6: all network IP
	press 7: enter domain name and find information about that
	'''
	print option


# (choice 1)Search input data in google
def search_input_in_google():
	search_data=raw_input("enter data...")
	final_data=search_data.strip() #removing all the unnecessary spaces in data
	
	done_data=final_data.split()  #split data by space so that can get each word and assigning into tuple
	os.system("firefox")
	time.sleep(2)
	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)	

# (choice 2)Scrape url from given web page
def scrap_url_from_webpage():

	url = raw_input("Enter the url of web page for url Scraping....")
	r = requests.get("http://"+url) #requesting webpage
	data = r.text	#converting web page data as a text 
	soup = BeautifulSoup(data)  #parsing data
		
	i=1 #for giving all url a Sequence number
	for link in soup.find_all('a'):
		print (" "+str(i)+" "+link.get('href'))
		print "                                                       "
		print "*******************************************************"
		i += 1  #increment in i's value
	


# (choice 3)Search Images for input data in google
def search_image_in_google():
	search_data=raw_input("enter data...")
	final_data=search_data.strip() #removing all the unnecessary spaces in data
	done_data=final_data.split()  #split data by space so that can get each word and assigning into tuple
	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i           +'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwib5u78qYnbAhWBLY8KHVNUBCwQ_AUIDSgE&biw=1366&bih=596') 	

def domain_info():
	domain_name = raw_input('\n\tEnter Domain Name : ')
	output = commands.getoutput(" whois "+domain_name)   #will execute command on terminal and will return output 
	required_data = output.split('<<<')        #for printing only required data(removing unnecessary information)
	print "\t\t+------------------------------------------------------------+"
	print "\t\t|			Domain_Information		     |"
	print "\t\t+------------------------------------------------------------+\n"
	print "###############################################################################################"
	print required_data[0]
	print "###############################################################################################"
	

#main function from where whole program will control
def main():
	google_search_menu()
	#take input choice of user
	ch=raw_input()
	if ch == '1' :
		search_input_in_google()
	elif ch == '2':
		scrap_url_from_webpage()
	elif ch == '3' : 
		search_image_in_google() 	
	elif ch == '4' :
		print "current date and time : "
		print str(datetime.datetime.now()) 
	elif ch == '5' :
		webbrowser.open_new("file:///usr/share/doc/HTML/en-US/index.html")
	elif ch == '7' :
		domain_info()
	else:
		print "no chance.."



#function calling

main()











