#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Counting unique URL

import sys
import fileinput
import platform

# Sets the output file.
out_file = open("map_url_out.txt", "w")

# Checks which platform is in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin
    
# Loop in the log file    
for line in inputdata:

    # Splits the line to get the URL.
    sURL = line.split('\t')[1]
    print ("%s" % (sURL))
    out_file.write("%s\n" % (sURL))

# Close output file.
out_file.close()

