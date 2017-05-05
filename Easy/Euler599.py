#!/usr/bin/env pypy

from math import factorial

choose = lambda n, k: factorial(n) / factorial(k) / factorial(n-k)
donut  = lambda k, n: choose(n+k-1, n)

def e599(Q = 10):
	corners = Q + Q*(Q-1) + Q*(Q-1)*(Q-2)/3
	ret = 3*donut(corners-Q, 8)
	for x in xrange(1, 9):
		q = donut(Q, x)*donut(corners-Q, 8-x)
		ret += q
	return ret

print e599()
