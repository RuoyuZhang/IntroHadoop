#!/usr/bin/python

import sys

numTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNum = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", numTotal
        oldKey = thisKey;
        numTotal = 0

    oldKey = thisKey
    numTotal += int(thisNum)

if oldKey != None:
    print oldKey, "\t", numTotal

