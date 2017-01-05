#!/usr/bin/pypy
#Euler 65
from math import sqrt, e as E
from fractions import Fraction as F, gcd
from operator import mul

def converge(arr):
	ret = 0
	for e in reversed(arr):
		ret = F(1, e+ret)
	return F(1, ret)

def q(s):
	e, r, t = 1, 1, -int(sqrt(s))
	past = [-t]
	while True:
		a = int(e / (r*sqrt(s)+t))
		yield converge(past)
		
		b, c, d = -e*t, r*r*s - t*t, e*r
		e, r, t = c, d, b - a*c
		
		g = gcd(e, gcd(r, t))
		e, r, t = e/g, r/g, t/g
		
		past.append(a)

def fundamentalpair(D):
	for pot in q(D):
		if pot.numerator**2 - D*pot.denominator**2 == 1:
			return pot.numerator, pot.denominator

def e66(L=1000):
	maxd, maxx = None, None
	for d in xrange(2, L+1):
		if d != int(sqrt(d))**2:
			x, y = fundamentalpair(d)
			if maxx is None or x > maxx:
				maxd, maxx = d, x

	return maxd

print e66()
