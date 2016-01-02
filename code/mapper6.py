#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip, iden, user, date, zone, method, path, query, status, size = data
	path = path.replace("http://www.the-associates.co.uk","")
        print "{0}".format(path)

