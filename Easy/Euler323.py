#!/usr/bin/env pypy
from math import factorial
from fractions import Fraction as F
from itertools import count

def mmul(A, B):
	m, k, n = len(A), len(B), len(B[0])
	return [[sum(A[r][e]*B[e][c] for e in xrange(k)) for c in xrange(n)] for r in xrange(m)]

def e323():
	#terrible markov matrix solution
	A = []
	for n in xrange(33):
		row = []
		for k in xrange(n+1):
			row.append(F(factorial(n), factorial(k)*factorial(n-k)*(1<<n)))
		for k in xrange(n+1, 33):
			row.append(0)
		A.append(row)

	last = 0
	Q = A
	ret = 0
	for x in xrange(1, 50):
		d = Q[-1][0]-last
		ret += x*d
		#~ print x, float(d), float(x*d), float(ret)
		last = Q[-1][0]
		Q = mmul(Q, A)

	print float(ret)

e323()
