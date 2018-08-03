#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Mapping user Clicks by URL

import sys
import fileinput
import platform

# Sets the output file.
#out_file = open("map_click_out.txt", "w")

# Checks which platform is in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin
    
# Loop in the log file    
for line in inputdata:

    # Split the line to get the Click, URL and User.
    sClick, sURL, sUser  = line.strip().split('\t')
    print ("%s\t%s\t%s" % (sURL, sUser, sClick))
    #out_file.write("%s\t%s\t%s\n" % (sURL, sUser, sClick))

#out_file.close()

