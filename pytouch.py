#!/usr/bin/python

import sys
from os import path

def touch_fun(f_name) :
	if path.exists(f_name) :
		print "pytouch: "+f_name+" :already exists "
	else :
		f=open(f_name,'w+')
		f.close()

file_name = sys.argv[1:]

for f in file_name :
	touch_fun(f)
