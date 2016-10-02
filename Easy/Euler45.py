#!/usr/bin/env pypy

from Lib import quad, isint
from itertools import count

def isPent(p):
	s = quad(3, -1, -2*p)
	return s and isint(s[0])

def isHex(h):
	s = quad(2, -1, -h)
	return s and isint(s[0])

def e45():
	T = 0
	for x in count(1):
		T += x
		if T>40755 and isPent(T) and isHex(T):
			return T

print e45()

'''
P(n) = n(3n-1)/2
0 = 3n^2 - n - 2P(n)

H(n) = n(2n-1)
0 = 2n^2 - n - H(n)
'''
