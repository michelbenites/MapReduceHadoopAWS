#!/usr/bin/python

import sys
import fileinput
import platform

# Set the variables.
last_hour     = None
last_url      = ""
last_user     = ""
current_count = 0

# Checks which platform is in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin
    
# Loop in the log file    
for line in inputdata:
    try:
        # Split the line to get hour, url and user
        sHour, sURL, sUser = line.strip().split('\t')
        # Check if currente URL is not "None".
        if not last_hour:
            last_hour = sHour
            last_url  = sURL
            last_user = sUser

        # If hour, url and user are the same as the previous ones, so add 1 to counter 
        if sHour == last_hour and sURL == last_url and sUser == last_user:
            current_count += 1
 
        else:
            # Else print the last values.
            print ('%s\t%s\t%s\t%d' % (last_hour, last_url, last_user, current_count))
            last_hour     = sHour
            last_url      = sURL
            last_user     = sUser
            current_count = 1          
        
    except ValueError as e:
        continue

#if current_count > 1:
print ('%s\t%s\t%s\t%d' % (sHour, sURL, sUser, current_count))
