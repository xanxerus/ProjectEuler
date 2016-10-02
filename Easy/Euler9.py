#!/usr/bin/env pypy

'''
a^2 + b^2 = c^2
a^2 = c^2 - b^2
a^2 = (c-b)(c+b) = xy
x+y = 2c
y-x = 2b
a + b + c = a + y

'''

from math import sqrt

def e9(L=1000):
	for a in xrange(2, L+1, 2):
		for x in xrange(2, 1+a, 2):
			if a*a%x==0:
				y = a*a/x
				if not y&1 and a+y == L:
					return a*(x+y>>1)*(y-x>>1)

print e9()
