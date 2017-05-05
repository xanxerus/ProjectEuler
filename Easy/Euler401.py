#!/usr/bin/env pypy

from math import sqrt

def squares(b, a=0):
	if a:
		return squares(b) - squares(a-1)
	else:
		return b*(b+1)*(2*b+1)/6

def e401(N=10**15, M=10**9):
	ret = 0
	last = N
	d = 1
	while True:
		pot = N//d
		ret += (d-1)*squares(last, pot+1)

		if pot == d:
			ret += d*d*pot
			break
		if pot < d:
			break

		ret += d*d*pot
		last = pot
		d += 1

	return ret

print e401()
#~ for x in xrange(1, 10):
	#~ print x, e401(x)
