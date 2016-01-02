#!/usr/bin/python
import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	
    for line in reader:
		if line[0] == "id":
			continue

		aid, atime = (line[3], line[8])
#		print atime
		time = atime.strip().split()[1]
		hour = time.split(':')[0]
		print aid, "\t", hour		

	


def main():
    mapper()

if __name__ == "__main__":
    main()

