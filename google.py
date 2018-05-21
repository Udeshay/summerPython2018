#!user/etc/python

import time     #for time function like sleep() etc
import webbrowser  #for accessing webbrowser from programe
import datetime	   #for fetching current time and date
from bs4 import BeautifulSoup  #for scraping data from web page
import requests  #for sending requesting for a specific url on browser but without opening that




#main menu to show user
def google_search_menu():
	option = '''
	press 1: to enter anything- split each word and search on google
	press 2: same but find URL
	press 3: same but find image answer
	press 4: current time and date
	press 5: open default browser
	press 6: all network IP
	press 7: enter domain name and find owner,email,contact
	'''
	print option


# (choice 1)Search input data in google
def search_input_in_google():
	search_data=raw_input("enter data...")
	final_data=search_data.strip() #removing all the unnecessary spaces in data
	
	done_data=final_data.split()  #split data by space so that can get each word and assigning into tuple


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
		webbrowser.open_new_tab('https://www.google.com/search?q='+i								              +'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwib5u78qYnbAhWBLY8KHVNUBCwQ_AUIDSgE&biw=1366&bih=596') 	

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
	else:
		print "no chance.."



#function calling

main()











