#!/usr/bin/env pypy
from Lib import cfcs

def e57():
	ret = 0
	c = cfcs(2)
	for i in xrange(1000):
		n, d = next(c)
		if len(str(n)) > len(str(d)):
			ret += 1
	return ret

print e57()
