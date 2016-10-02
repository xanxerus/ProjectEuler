#!/usr/bin/env pypy

#brute force

from math import sqrt

def ispandigital(s):
	if len(s) != 9 or '0' in s:
		return False
	for x in '123456789':
		if not x in s:
			return False
	return True

def can(n):
	for x in range(1, 1 + int(sqrt(n))):
		if n%x == 0 and ispandigital(str(x)+str(n/x)+str(n)):
			return True
	return False

print sum(x for x in xrange(10**4) if can(x))
