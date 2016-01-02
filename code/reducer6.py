#!/usr/bin/python

import sys

access = 0
high = 0
path = None
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()
    #if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
    #    continue

   # thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", access
	if access > high:
	    high = access
	    path = oldKey

        oldKey = thisKey;
        access = 0

    oldKey = thisKey
    access += 1

if oldKey != None:
    if access > high:
	high = access
	path = oldKey

print path, "\t", high

