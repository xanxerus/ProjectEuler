#!/usr/bin/env pypy

def e28(L=1001):
	ret = 1
	for x in xrange(3, L+1, 2):
		s = x*x
		d = x-1
		ret += s + s-d + s-2*d +s-3*d
	return ret

print e28()
