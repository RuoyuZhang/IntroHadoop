#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    data = line.strip()
    #nodes = re.split('[\s\.,!?:;"\(\)<>\[\]#\$\=-\/]',data)
    nodes = re.split('[\s+\.,!\?:;\"\(\)<>\[\]#\$\=\-\/]',data)
    while '' in nodes:
	nodes.remove('')
    #print nodes
#    if len(data) == 10:
    arr_appear = dict((a, nodes.count(a)) for a in nodes); 
    for a in arr_appear.keys():
	print a, "\t", arr_appear[a]
