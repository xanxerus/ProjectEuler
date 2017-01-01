#!/usr/bin/pypy
#Euler 60
from math import sqrt
from time import time

def isprime(n):
	if n < 4:
		return n > 1
	if n%2==0 or n%3==0:
		return False
	for x in xrange(5, int(sqrt(n))+1, 6):
		if n%x == 0 or n%(x+2) == 0:
			return False
	return True

def era(n):
	arr = [0,0]+range(2, n+1)
	for x in arr:
		if x:
			for y in xrange(x<<1, n+1, x):
				arr[y] = 0
	return filter(None, arr)

cache = dict()
def connects(x, y):
	if (x, y) in cache:
		return cache[(x, y)]
	else:
		ret = isprime(int('%d%d' % (primes[x], primes[y]))) and isprime(int('%d%d' % (primes[y], primes[x])))
		cache[(x, y)] = ret
		return ret

M = 5
L = 10**M
primes = era(L)
arr = [set() for x in xrange(L+1)]
print 'era'
t = time()
soln = None
def recur(sofar=None):
	global soln
	if sofar is None:
		sofar = []
	
	if soln is None or sum(sofar) < sum(soln):
		if len(sofar) < M:
			for y in xrange(sofar[-1]+1 if sofar else 0, len(primes)):
				for x in sofar:
					if not connects(x, y):
						break
				else:
					recur(sofar + [y])
		elif len(sofar) == M:
			soln = sofar
			print sum(primes[x] for x in sofar), [primes[x] for x in sofar], time()-t

recur()
#~ for x in xrange(1000):
	#~ print x, sum(primes[x:x+5])
