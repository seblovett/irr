#!/usr/bin/python
# @file watch.py
# Date Created: Wed 19 Feb 2014 09:53:17 GMT by <+AUTHORNAME+> on seblovett-Ubuntu
# <+Last Edited: Wed 19 Feb 2014 10:06:42 GMT by seblovett on seblovett-Ubuntu +>
# @author seblovett
# @brief A brief description of this code

## @brief Documentation for a function.
#  @param - None
#  @retval - None
#  More details.
import os
import time
from subprocess import call


def GetTexFilesDates():
	dates = dict()
	for f in files:
		if f.endswith(".tex"):
			dates[f] = os.path.getmtime(f)
	return dates
#	print texfiles

if "__main__" == __name__:
	''' Code to be run if this is main '''
	files = os.listdir(".")
	dates = GetTexFilesDates()
	print dates
	while True: #always
		newdates = GetTexFilesDates()
		for k in dates:
			if dates[k] != newdates[k]:
				print("Compiling...")
				call("./make.sh")
				break
		dates = newdates
		time.sleep(1)
		
	pass

