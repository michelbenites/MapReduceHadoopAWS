#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Get the TOP 5 url

import sys
import fileinput
import platform

# Sets the variables.
last_url      = None
current_count = 0
urllist       = []

# Checks which platform is in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin
    
# Loop in the log file    
for line in inputdata:
    try:
        # split the line to get URL and the counter.
        sURL, count = line.strip().split('\t')
        # Checks if current is the first round 
        if not last_url:
            last_url = sURL

        # Checks if current URL  is not equal the last url.....
        if sURL != last_url:
            # ....if so, append the url and counter on the list and restart the counter.
            urllist.append ([last_url, current_count])
            last_url       = sURL
            current_count  = 1
        else:
            # Else add 1 to counter.
            current_count += 1
            
            
    except ValueError as e:
        continue

# Appends the last value on the list.
urllist.append ([last_url, current_count])
urlsort = sorted(urllist,key=lambda x: x[1], reverse = True)

# Checks the size of list
if len(urlsort) < 5:
   size = len(urlsort)
else:
   size = 5

# Print the top 5 or less.
for i in range(size):
    print ('%s\t%d' % (urlsort[i][0], urlsort[i][1]))
    
