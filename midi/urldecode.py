#!/usr/bin/env python

import urllib
import sys

with open (sys.argv[1], "r") as myfile:
    data=myfile.read()
    print "input data: " + data
    decoded = urllib.unquote(data)
    with open(sys.argv[1] + ".mid", "w") as text_file:
        text_file.write("%s" % (decoded))
