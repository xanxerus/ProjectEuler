#!/usr/bin/pypy

from itertools import count
from math import sqrt

#naive primality test
def isprime(n):
	if n < 4:
		return n > 1
	if (n&1)==0 or n%3==0:
		return False
	for x in xrange(5, 1+int(sqrt(n)), 6):
		if n%x==0 or n%(x+2)==0:
			return False
	return True

def e516(L=10**12):
	#get a list of all q such that q is prime and q-1 is 5-smooth 
	smooth = set()
	pi = 1
	for i in count(0):
		if pi > L:
			break
		
		pj = pi
		for j in count(0):
			if pj > L:
				break
			
			pk = pj
			for k in count(0):
				if pk > L:
					break

				if isprime(pk+1):
					smooth.add(pk+1)
				
				
				
				pk *= 5
			pj *= 3
		pi <<= 1

	#obviously we don't want 2, 3, 5
	smooth -= {2, 3, 5}
	#~ print len(smooth)

	#find all products of these q
	smooth = sorted(smooth)
	newsmooth = set()
	def smoothen(n=1, i=0):
		for i in xrange(i, len(smooth)):
			x = smooth[i]
			if x*n <= L:
				newsmooth.add(x*n)
				smoothen(x*n, i+1)
			else:
				break
	smoothen()
	smooth = sorted(newsmooth)

	#sum all things of the form 2^i * 3^j * 5^k * q1 * q2 * ... * qn
	s = 0
	pi = 1
	for i in count(0):
		if pi > L:
			break
		
		pj = pi
		for j in count(0):
			if pj > L:
				break
			
			pk = pj
			for k in count(0):
				if pk > L:
					break
				
				#~ print pk, i, j, k
				
				s += pk
				for x in smooth:
					if pk*x <= L:
						s += x*pk
					else:
						break
				
				s &= (1<<32)-1
				
				pk *= 5
			pj *= 3
		pi <<= 1

	return s

print e516()
