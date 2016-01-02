#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
	salesmean = salesTotal/count
        print oldKey, "\t", salesmean
        oldKey = thisKey;
        salesTotal = 0
	count=0

    oldKey = thisKey
    salesTotal += float(thisSale)
    count += 1

if oldKey != None:
    salesmean = salesTotal/count	
    print oldKey, "\t", salesmean

