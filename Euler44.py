#!/usr/bin/env pypy

from Lib import quad, isint
from math import sqrt
from itertools import count

def toPent(n):
	return n*(3*n-1)>>1

def isPent(p):
	s = quad(3, -1, -2*p)
	return s and isint(s[0])

def e44():
	for n in count(1):
		for k in range(1, n):
			a, b = toPent(k), toPent(n)
			if isPent(b-a) and isPent(b+a):
				return toPent(n) - toPent(k)

print e44()

'''
P(n) - P(k) = P(a)
P(n) + P(k) = P(b)

a < b
k < n
'''
