#!/usr/bin/pypy
from operator import mul
from collections import Counter
from time import time
from itertools import count
from fractions import Fraction as F
import resource
import sys

# Will segfault without this line.
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

M = 10**9
T = 4*10**8

def watch(fun, *args):
	t = time()
	return fun(*args), time()-t

def befac(L):
	ret = [dict() for x in xrange(L+1)]
	for x in xrange(2, L+1):
		if not ret[x]:
			ret[x] = {x:1}
			for y in xrange(x<<1, L+1, x):
				ret[y][x] = 0
				n = y
				while n > 1 and n%x == 0:
					n/=x
					ret[y][x] += 1
	return ret

def Le(n):
	ret = dict()
	facs = befac(n)
	for x in xrange(2, n+1):
		f = facs[x]
		for k in f:
			if f[k] > ret.get(k, 0):
				ret[k] = f[k]
	#~ print 'Le:', ret
	return [ret[x]+1 for x in ret]
	#~ return reduce(mul, (k**ret[k] for k in ret))

def B(e):
	sigcache = dict()
	def sigma(d, i, m):
		if (d, i, m) in sigcache:
			sigcache[(d, i, m)][1] += 1
			return sigcache[(d, i, m)][0]
		if d == 0:
			ret = pow(2, m%T, M)
		else:
			ret = sum(sigma(d-1, k+1, m*(e[k]-1)/e[k]) for k in xrange(i, len(e)-d+1))
		sigcache[(d, i, m)] = [ret, 1]
		return ret
	
	R = reduce(mul, e)
	ret = sum(sigma(k+1, 0, R) * pow(-1, k) for k in xrange(0, len(e)))
	return (pow(2, R%T, M) - ret) % M

def imp(e):
	R = reduce(mul, e, 1)
	e = [x-1 for x in e]
	m = list(set(e))
	c = [e.count(x) for x in m]
	
	def rick(p, d=0, l=0, w=1, q=R):
		#~ print '\t'*d, p
		ret = -w*pow(2, q%T, M) if d&1 else w*pow(2, q%T, M)
		#~ print '\t'*d, ('p: %s, l: %d, w: %s, q: %d, delta: %s' % (p, l, w, q, ret))
		for j in xrange(l, len(m)):
			if p[j]>0:
				ret += rick((p[:j] + (p[j]-1,) + p[j+1:]), d+1, j, w * F(p[j], c[j]-p[j]+1), q * m[j] / (m[j]+1))
		return ret%M
	
	return rick(tuple(c))

Q = imp
def H(n):
	return Q([x+1 for x in befac(n)[n].values()])

def HL(n):
	return Q(Le(n))

#~ print H(6)
#~ print H(12)
#~ print HL(4)
print HL(50000)

#~ cow = Le(50000)
#~ kitty = '[2]*5085 + [3]*37 + [4]*5 + [5]*2 + [16]*1 + [10]*1 + [7]*1 + [6]*1'
#~ print cow
