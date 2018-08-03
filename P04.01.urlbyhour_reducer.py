#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Counting uniques URL by Hour

import sys
import fileinput
import platform

# Checks which platform is in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin

# Sets variables.
last_hour     = None
last_url      = ""
current_count = 1

    
# Loop in the log file    
for line in inputdata:
    try:
        # Gets hour, url from line.
        sHour, sURL = line.strip().split('\t')
        
        # Check if currente URL is not "None".
        if not last_hour:
            last_hour = sHour
            last_url  = sURL
            
        # if hour is equal the last hour and url is not equal the last url, so add 1 to counter
        if sHour == last_hour:
            if sURL != last_url:
                current_count += 1
                last_url       = sURL
        else:
            # else print the last values.
            print ('%s\t%d' % (last_hour, current_count))
            last_hour     = sHour
            last_url      = sURL
            current_count = 1          
        
    except ValueError as e:
        continue

#if current_count > 1:
print ('%s\t%d' % (sHour, current_count))
