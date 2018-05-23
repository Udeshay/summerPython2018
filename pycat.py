#!/usr/bin/python

import sys

from os import path

#function definition of cat_fun
def cat_fun(f_name):
	if path.exists(f_name):
		if path.isfile(f_name):
			f = open(f_name,'r')  #opening file in read mode
			print f.read()  #will read file and print all data
			f.close()
		
		else :
			print "\n\tcatpy:"+f_name+":***Is a Directory***"
		
	else :
		print "\n\tcatpy:"+f_name+":***No such file or Directory***"


#taking input as command line-
file_name = sys.argv[1:]

for f in file_name:
	cat_fun(f)

