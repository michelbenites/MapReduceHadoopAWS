#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Mapping user and url

import sys

test = sys.argv[1]
count = int(test)

# Loop in the log file    
for line in sys.stdin:

    # Split the line to get the URL and User.
    sDummy, sURL, sUser = line.strip().split('\t')
    print ("%s\t%s\t%d" % (sURL, sUser, count))



##import sys
##import fileinput
##import platform
##
##
### Checks which platform is being in use.
##if platform.system() == "Windows":
##    inputdata = fileinput.input()
##    # Sets the output file.
##    out_file = open("map_user_out.txt", "w")
##else:
##    inputdata = sys.stdin
##
### Loop in the log file    
##for line in inputdata:
##
##    # Split the line to get the URL and User.
##    sDummy, sURL, sUser = line.strip().split('\t')
##    print ("%s\t%s\t%d" % (sURL, sUser, 1))
##    #setlist.append((sURL, sUser))
##
##    if platform.system() == "Windows":
##        out_file.write("%s\t%s\t%d\n" % (sURL, sUser, 1))
##
##if platform.system() == "Windows":
##    out_file.close()
