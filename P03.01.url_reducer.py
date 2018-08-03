#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Counting unique URL

import sys
import fileinput
import platform

# Checks which platform is being in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin

last_url = None
current_count = 1

# Loop in the map file.
for line in inputdata:
    # Gets the URL from line        
    sURL = line.strip().split('\t')
        
    # Checks if last URL is valid (!= None).
    if last_url:
        # If current URL is not equal of previous one, so add 1 to counter
        if sURL != last_url and sURL != "":
            current_count += 1
         
    last_url = sURL
    
print ("%d" % (current_count))
