#!user/etc/python

import time
import webbrowser

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

ch=raw_input()

if ch == '1' :
	search_data=raw_input("enter data...")
	final_data=search_data.strip() #removing all the unnecessary spaces in data
	
	done_data=final_data.split()  #split data by space so that can get each word and assigning into tuple


	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)							            

elif ch == '3' : 
	search_data=raw_input("enter data...")
	final_data=search_data.strip() #removing all the unnecessary spaces in data
	

	done_data=final_data.split()  #split data by space so that can get each word and assigning into tuple

	print done_data

	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i								              +'+Images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwib5u78qYnbAhWBLY8KHVNUBCwQ_AUIDSgE&biw=1366&bih=596') 	
else:
	print "no chance.."

