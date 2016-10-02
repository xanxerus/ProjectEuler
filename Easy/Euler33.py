#!/usr/bin/env pypy

from fractions import Fraction as F

ret = F(1)
for d in xrange(10, 100):
	for n in xrange(10, d):
		if n*(d%10) == d*(n//10) and n%10==d//10 or n*(d//10) == d*(n%10) and n//10==d%10:
			ret *= F(n, d)

print ret.denominator
