#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Counting user by hour

import sys
import fileinput
import platform

# Set the variables.
last_hour     = None
last_url      = ""
last_user     = ""
current_count = 1

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
        # If hour and url are the same as the previous one.... 
        if sHour == last_hour and sURL == last_url:
            # .... and the user is no equal the last, so add 1 to counter
            if sUser != last_user:
                current_count += 1
                last_user      = sUser                

        else:
            # Else print the last values
            print ('%s\t%s\t%d' % (last_hour, last_url, current_count))
            last_hour     = sHour
            last_url      = sURL
            last_user     = sUser
            current_count = 1          
        
    except ValueError as e:
        continue

print ('%s\t%s\t%d' % (sHour, sURL, current_count))
