#!/usr/bin/env python
## Traverse directory (including subdirectories) and delete files older than 30 days.

__author__ = "Forrest Dworsky"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "forrest.dworsky@gmail.com"
__status__ = "Production"

import sys
import os
from datetime import datetime
from datetime import timedelta
import glob
from math import sqrt

THIS_SCRIPT = sys.argv[0] #global var to represent this script.  sys.argv[0] always refers to the file being executed

# 0. Enumerate Directory
def dirwalk(filepath):
	# INSERT ERRROR HANDLER FOR OSERROR HERE #
	
	#print os.walk(filepath)
	# 1. go down subdirectories (if present)
	old_files = dict() #initialize dictionary
	for root, dirs, files in os.walk(filepath):
		print("******************************************")
		print("Current directory: " + root)
		for f in files:
			fn = root+'/'+f #specify the root directory so that the program can find the files
			stamp = os.path.getmtime(fn) #get the date modified of the files being listed
			current_epoch = datetime.now().timestamp()
			print("File " + f + " timestamp: " + datetime.fromtimestamp(stamp).strftime("%A, %B %d, %Y %H:%M:%S"))
			thirtydays = timedelta(days=30).total_seconds() #make a var for 30 days
			if (stamp < (current_epoch-thirtydays)) and f != THIS_SCRIPT: old_files[fn] = stamp #if the date modified is greater than 30 days and the file is not the script being run
	return old_files #return the old_files so it can be used

## TO DO ##
def file_deleter(old_files):
	#print("******************************************")
	print("**File Deletion Section**")
	for f,s in old_files.items():
		#iterate through the key, value in the dictionary.  That's why we need the two variables
		date = datetime.fromtimestamp(s).strftime("%A, %B %d, %Y %H:%M:%S")
		#make a var for the formatted date of the files
		print("Files to be Deleted:")
		print(f+' '+date)

# 3. Gotcha: ARE YOU SURE YOU WANT TO DO THIS!?! List files to be deleted
## and prompt user (y/n)?
	user_in = 'x' #initialize the user input.  we won't actually use x
	while user_in != 'y' and user_in != 'n':
		user_in = input("Are you sure you want to delete these files? Respond 'y' or 'n'")
		#use a while loop so that the prompt will keep repeating until the user says y or n

# 4. Delete Files (or die if no)
	if user_in == 'y':
		print("Files are being deleted.")
		for f,s in old_files.items():
			print("Deleting: " + f)
			os.remove(f)
	
	return

def main(argv):
	filepath = argv[1]
	old_files = dirwalk(filepath)
	file_deleter(old_files)

if __name__=="__main__":
    main(sys.argv)