#!/usr/bin/env pypy

def e56():
	return max(sum(int(c) for c in str(a**b)) for a in xrange(1, 101) for b in xrange(1, 101))

print e56()
