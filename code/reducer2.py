#!/usr/bin/python

import sys

salesHigh = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesHigh
        oldKey = thisKey
        salesHigh = 0

    oldKey = thisKey
    if salesHigh < float(thisSale):
	salesHigh = float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesHigh

