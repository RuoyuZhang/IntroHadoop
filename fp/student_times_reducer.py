#!/usr/bin/python

import sys

hourHigh = 0
hours = []
hourCount = 0
oldKey = None
oldHour = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    
    thisKey, thisHour = data_mapped

    if oldKey and oldKey != thisKey:

        if hourCount > hourHigh:
            hourHigh = hourCount
            hours = [oldHour]
        elif hourCount == hourHigh:
            hours.append(oldHour)
        
        for item in hours:
            print oldKey, "\t", item
        oldKey = thisKey;
        hourHigh = 0
        hours = []
        hourCount = 0

    oldKey = thisKey
	
    if oldHour and oldHour != thisHour:
        if hourCount > hourHigh:
            hourHigh = hourCount
            hours = [oldHour]
        elif hourCount == hourHigh:
            hours.append(oldHour)
		
        hourCount = 0
	
    oldHour = thisHour			
    hourCount += 1

if oldKey != None:
    if hourCount > hourHigh:
        hourHigh = hourCount
        hours = [oldHour]
    elif hourCount == hourHigh:
        hours.append(oldHour)
	
    for item in hours:
        print oldKey, "\t", item
