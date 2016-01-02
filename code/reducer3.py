#!/usr/bin/python

import sys

salesTotal = 0
salesNum = 0

for line in sys.stdin:
    thisSale = line.strip()
    #print len(thisSale)
    #if len(thisSale) != 1:
        # Something has gone wrong. Skip this line.
    #    continue

    salesNum += 1
    salesTotal += float(thisSale)

print salesTotal, "\t", salesNum

