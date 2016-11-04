#!/usr/bin/env pypy

def e55(L=10**4):
	ret = 0
	for x in xrange(L):
		for i in xrange(50):
			x = x + int(str(x)[::-1])
			if str(x) == str(x)[::-1]:
				break
		else:
			ret += 1
	return ret

print e55()
