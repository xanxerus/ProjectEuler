#!/usr/bin/env pypy

from math import factorial

def r(i=9, s=0, n=10, p=10):
	if i:
		ret = 0
		if n>1:
			ret += r(i-1, s-i-i, n-2, p)/2
		if p>1:
			ret += r(i-1, s+i+i, n, p-2)/2
		if n and p:
			ret += r(i-1, s, n-1, p-1)
		return ret
	else:
		if s%11 == 0:
			if n == 2:
				return 8*factorial(9)*factorial(10)/2
			if n == 1:
				return 9*factorial(9)*factorial(10)
			else:
				return factorial(10)**2/2
			return 1
		else:
			return 0

print r()
