#!/usr/bin/pypy
#Euler 62

from itertools import count

d = dict()

for x in count(1):
	s = ''.join(sorted(str(x**3)))
	d[s] = d.get(s, []) + [x]
	if len(d[s]) == 5:
		print d[s][0]**3
		break
