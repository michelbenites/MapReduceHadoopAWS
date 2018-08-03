#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Mapping Hour and URL

import sys
import fileinput
import platform
from datetime import datetime

# Sets the output file.
#out_file = open("map_urlbyhour_out.txt", "w")

# Checks which platform is in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin
    
# Loop in the log file    
for line in inputdata:

    # Split the line to get the Hour and URL
    sHour, sURL, sDummy = line.split('\t')
    # Get only 19 first character and convert to date 
    sHour = sHour[:19]
    dHour = datetime.strptime(sHour, '%Y-%m-%dT%H:%M:%S')
    sHour = datetime.strftime(dHour, '%Y-%m-%d %Hh') 
    print ("%s\t%s\t" % (sHour, sURL))
    #out_file.write("%s\t%s\n" % (sHour, sURL))

#out_file.close()

