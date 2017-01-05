#!/usr/bin/pypy
#Euler 64
from math import sqrt
from fractions import Fraction as F, gcd

def q(s):
	e, r, t = 1, 1, -int(sqrt(s))
	past = [(e, r, t)]
	while True:
		a = int(e / (r*sqrt(s)+t))
		b, c, d = -e*t, r*r*s - t*t, e*r
		e, r, t = c, d, b - a*c
		
		g = gcd(e, gcd(r, t))
		e, r, t = e/g, r/g, t/g
		
		if (e, r, t) in past:
			return len(past) - past.index((e, r, t))
		
		past.append((e, r, t))

def e64(L=10000):
	ret = 0
	for x in xrange(2, L+1):
		if x != int(sqrt(x))**2 and q(x)&1:
			ret += 1
	return ret

print e64()
