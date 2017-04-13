#!/usr/bin/pypy
from fractions import gcd
from math import sqrt

def e504(L):
	ret = 0
	for b in xrange(1, L+1):
		for d in xrange(b, L+1):
			for a in xrange(1, L+1):
				for c in xrange(a, L+1):
					I = (b+d)*(a+c) - gcd(a, b) - gcd(b, c) - gcd(c, d) - gcd(d, a) + 2 >> 1
					if I == int(sqrt(I))**2:
						if a == c and b == d:
							ret += 1
						elif (a == c) ^ (b == d):
							ret += 2
						else:
							ret += 4
	return ret

print e504(100)
