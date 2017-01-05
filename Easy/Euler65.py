#!/usr/bin/pypy
#Euler 65
from fractions import Fraction as F

def r(L, depth=0):
	if depth >= L:
		return 0
	elif depth == 0:
		p = r(L, depth+1)
		return 2 + (F(1, p) if p else 0)
	elif depth%3 == 2:
		p = r(L, depth+1)
		return 2*(depth+2)/3 + (F(1, p) if p else 0)
	else:
		p = r(L, depth+1)
		return 1 + (F(1, p) if p else 0)

print sum(int(c) for c in str(r(100).numerator))
