#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Mapping URL

import sys
import fileinput
import platform

# Sets the output file.
#out_file = open("map_topurl_out.txt", "w")

# Checks which platform is in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin
    
# Loop in the log file    
for line in inputdata:

    # Split the line to get the URL
    sDummy, sURL, sDummy = line.strip().split('\t')
    print ("%s\t%d" % (sURL, 1))
 #   out_file.write("%s\t%d\n" % (sURL, 1))

#out_file.close()
#print ("Mapper is done")
