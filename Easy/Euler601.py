#!/usr/bin/env pypy

# I'm lazy and stole the gcd and lcm from this gist: 
# https://gist.github.com/endolith/114336

def gcd(*numbers):
	"""Return the greatest common divisor of the given integers"""
	from fractions import gcd
	return reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:

def lcm(*numbers):
	"""Return lowest common multiple."""    
	def lcm(a, b):
		return (a * b) // gcd(a, b)
	return reduce(lcm, numbers, 1)

def P(s, N):
	q = lcm(*range(2, s+1))
	w = lcm(*range(2, s+2))
	
	#~ print '\t', s, N, ':', q, w, N//q, N//w, N//q - N//w
	
	return N//q - N//w + (1 if N%q!=0 else 0) - (1 if N%w!=0 else 0)

print sum(P(i, pow(4, i)-1) for i in xrange(1, 32))
