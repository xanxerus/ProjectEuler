#!/usr/bin/env pypy
from fractions import Fraction as F
from operator import mul
from math import sqrt
from time import time

t = time()
MMI = lambda A,n,s=1,t=0,N=0: (n<2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
concat = lambda *args: int(''.join(map(str, args)))

'''primal'''
beprimes = [] #list of all calculated primes

def begetprimes():
	return beprimes

def era(L, verbose=False): #segmented sieve of eratosthenes
	global beprimes
	
	if verbose:
		print 'Calculating primes to', L
	
	if beprimes and L < beprimes[-1]: #already calculated
		for i in range(len(beprimes)):
			if beprimes[i] > L:
				break
		
		if verbose:
			print 'Already calculated'
		
		return beprimes[:i]
	
	if L <= 10**7: #small enough, no segmentation
		ret = [0, 0] + range(2, L+1)
		for x in ret:
			if x:
				beprimes.append(x)
				for y in xrange(x<<1, L+1, x):
					ret[y] = 0
		
		if verbose:
			print 'Trivial limit %d of primes calculated' % L
		
		return beprimes
	else: #too big, needs segmentation
		s = beprimes[-1] if beprimes else 0
		for i in xrange((L-s)/10**7 + 1):
			beextend(verbose)
		return era(L, verbose)

def beextend(verbose=False): #builds the next segment of primes
	global beprimes
	if not beprimes:
		era(10**7, verbose)
	else:
		q = beprimes[-1]+1
		L = q + 10**7
		
		if verbose:
			print 'Extending prime list to %d -- %f' % (L, time()-t)
		
		arr = range(q, L+1)
		for p in beprimes:
			for y in xrange(q - q%p, L+1, p):
				if y>=q:
					arr[y-q] = 0
		for x in arr:
			if x:
				beprimes.append(x)
				for y in xrange(x<<1, L+1, x):
					arr[y-q] = 0

def awesometotient(L): #totient sieve
	ret = range(L+1)
	for x in xrange(2, L+1):
		if isinstance(ret[x], int):
			ret[x] -= 1
			for y in range(x<<1, L+1, x):
				if isinstance(ret[y], int):
					ret[y] = {x}
				else:
					ret[y].add(x)
		else:
			ret[x] = reduce(mul, (F(p-1, p) for p in ret[x]), x).numerator
	return ret

def besieve(L): # {base:exponent, ...} prime factorization sieve
	arr = [None, None] + range(2, L+1)
	for x in xrange(2, L+1):
		if isinstance(arr[x], int):
			arr[x] = {x:1}
			for y in xrange(x<<1, L+1, x):
				if isinstance(arr[y], int):
					arr[y] = behm(y, x)
				else:
					arr[y][x] = hm(y, x)
	return arr

def isprime(n, sieve=False): #naive prime test, uses precalculated primes if possible
	if n < 4: 
		return n > 1
	if n%2==0 or n%3==0: 
		return False
	if beprimes and n <= beprimes[-1]:
		return n in beprimes

	s = int(sqrt(n))
	x = 5
	for x in beprimes:
		if x > s:
			return True
		elif n%x==0:
			return False

	if sieve:
		beextend()
		return isprime(n, sieve)

	while x%6!=5:
		x+=1

	for x in range(x, 1+s, 6):
		if n%x==0 or n%(x+2)==0:
			return False
	else:
		return True

def nextprime(n): #duh
	if n < 2:
		return 2
	elif n < 3:
		return 3
	elif n < 5:
		return 5
	
	n += 1
	while n%6 not in (1, 5):
		n += 1
	
	q = n%6
	while not isprime(n):
		n += 4 if q == 1 else 2
		q = 1 if q == 5 else 5
	return n

def befactorize(n, sieve=False, start=2): #naive prime factorization
	if n == 1:
		return dict()
	elif n < 1:
		return None
	
	ret = dict()
	
	if start<=2:
		pot = hm(n, 2)
		if pot:
			ret[2] = pot
			n >>= pot
		start = 3
	
	if start<=3:
		pot = hm(n, 3)
		if pot:
			ret[3] = pot
			n /= 3**pot
		start = 5

	for p in beprimes:
		if n <= 1:
			break
		
		if p >= start:
			pot = hm(n, p)
			if pot:
				ret[p] = pot
				n /= p**pot
			start = p

	if sieve and n > 1:
		beextend()
		return merge(ret, befactorize(n, sieve, start))
	elif n>1:
		p = beprimes[-1] if beprimes else 5
		while not isprime(p):
			p += 1
		while n > 1:
			q = behm(n, p)
			if q[p] > 0:
				ret = merge(ret, q)
				n /= bemul(q)
			
			p += 2 if p%6==5 else 4
			while not isprime(p):
				p += 2 if p%6==5 else 4

	return ret

def merge(a, b): #combine two dicts, adding values where keys collide
	ret = dict(a)
	for k in b:
		ret[k] = ret.get(k, 0) + b[k]
	return ret

def hm(y, x): # exponent of the least x^k | y
	ret = 0
	if x==2:
		while y&1==0:
			y>>=1
			ret+=1
	else:
		while y%x==0:
			y/=x 
			ret+=1
	return ret

def behm(y, x):
	return {x: hm(y, x)}

def bemul(d): # given {a:x, b:y, c:z, ... }, return a^x * b^y * c^z * ...
	if len(d) == 0:
		return 1
	return reduce(mul, (pow(k, d[k]) for k in d))

def bearrmul(p, k): # given [a, b, c, ...] and [x, y, z, ...], return a^x * b^y * c^z * ...
	if min(len(p), len(k)) == 0:
		return 1
	return reduce(mul, (p[i]**k[i] for i in range(min(len(p), len(k)))))

def bearrfacs(d): #number of factors of a number
	if len(d) == 0:
		return 1
	else:
		return reduce(lambda a,b: a*(b+1), d, 1)

def begcd(a, b, sieve=False): # gcd of two numbers
	if isinstance(a, int): a = befactorize(a, sieve)
	if isinstance(b, int): b = befactorize(b, sieve)
	ret = dict()
	for k in a:
		if k in b:
			ret[k] = min(a[k], b[k])
	return ret

def bedecorate(fun): #just read the code -- it's a decorator
	def hjalp(d, sieve=False, *args):
		if not isinstance(d, dict):
			d = befactorize(d, sieve)
		return fun(d, *args)
	return hjalp

@bedecorate
def befacs(d): #number of factors of a number
	if len(d) == 0:
		return 1
	else:
		return reduce(lambda a,b: a*(b+1), d.values(), 1)

@bedecorate
def befaclist(d): #list of factors of a number
	p = d.keys()
	k = d.values()
	for e in incgen(k):
		yield bearrmul(p, e)

@bedecorate
def beppwrs(d): #list of prime power factors of a number
	return list(p**d[p] for p in d)

def naivetotient(n, d=None, sieve=False): #it's a totient function.
	if n == 1:
		return 1
	
	if d is None:
		if isinstance(n, int):
			d = befactorize(n, sieve)
		else:
			n, d = bemul(n), n

	return reduce(mul, (F(p-1, p) for p in d), n).numerator

'''iterative'''

def incgen(lim): #multiradix counter with reversed digits
	ret = [0]*len(lim)
	while True:
		yield ret
		i = 0
		while ret[i] == lim[i]:
			i += 1
			if i >= len(lim):
				raise StopIteration
		ret[i] += 1
		while i > 0:
			i -= 1
			ret[i] = 0

def xcount(arg1, arg2=None, step=None): #like xrange, but accepts floats
	start = 0 if arg2 is None else arg1
	stop = arg1 if arg2 is None else arg2
	stop = 1 if step is None else step
	while start < stop:
		yield start
		start += step

'''recursive'''

def memoize(fun): #duh
	cache = dict()
	def hjalp(*args):
		if args in cache:
			return cache[args]
		ret = fun(*args)
		cache[args] = ret
		return ret
	return hjalp

def nonhashmemoize(fun): #memoize by hashing the string of the args tuple
	cache = dict()
	def hjalp(*args):
		k = str(args)
		if k in cache:
			return cache[k]
		ret = fun(*args)
		cache[k] = ret
		return ret
	return hjalp

def jack(n, p, e): #p**e if p**e < n else 0
	if e == 0:
		ret = 1
	elif e&1:
		ret = p*jack(n, p, e-1)
	else:
		ret = jack(n, p, e>>1)**2
	return 0 if n < ret else ret

'''diophantine'''

def eea(a, b, c=1, verbose=False): #euclidean algorithm: solve ax + by = c
	a = [a, b]
	d = []
	i = 0
	while a[i]%a[i+1]:
		d.append(a[i]/a[i+1])
		a.append(a[i]%a[i+1])
		if verbose:
			print '%d = %d * %d + %d' % (a[i], a[i+1], d[i], a[i+2])
		i += 1

	if verbose:
		print '%d = %d * %d + %d' % (a[i], a[i+1], a[i]/a[i+1], a[i]%a[i+1])
		print

	d += [1]
	
	if c%a[-1] != 0:
		if verbose:
			print '%d % %d != 0' % (c, a[-1])
		return None
	
	A, Q, B, D = a[i-1], d[i], a[i], -d[i-1]
	while i > 1:
		G, K = a[i-2], -d[i-2]
		if verbose:
			print '%d = %d * %d + %d * %d' % (a[-1], A, Q, B, D)
			print '%d = %d + (%d + %d * %d) * %d' % (a[-1], A, G, A, K, D)
		A, Q, B, D = G, D, A, D*K + Q
		i -= 1
	q = c/a[-1]
	if verbose:
			print '%d = %d * %d + %d * %d' % (a[-1], A, Q, B, D)
			print '%d / %d = %d' % (c, a[-1], q)
			print '%d = %d * %d + %d * %d' % (q*a[-1], A, q*Q, B, q*D)
	return Q*q, D*q, a[-1] #x, y, gcd(a, b)


def cfcs(n): #continued fraction convergents for sqrt(n)
	s = n**.5
	past = []
	
	a = t = int(s)
	r = 1
	
	while True:
		past.append(a)
		ret = reduce(lambda a, b: F(a.denominator, a.numerator + b*a.denominator), reversed(past[:-1]), F(1, past[-1]))
		yield ret.denominator, ret.numerator
		e = n - t*t
		a = int(r*(s+t)/e)
		r, t = e/r, abs(t - a*e/r)

def pellfundamentalpair(D, c=1): #fundamental x, y for x^2 - D*y^2 == 1
	for h, k in cfcs(D):
		if c == h*h - D*k*k:
			return h, k

def pellsolutions(n, c=1): #infinitely many solutions to y^2 - D*x^2 == c
	x1, y1 = pellfundamentalpair(n, c)
	xk, yk = x1, y1
	while True:
		yield xk, yk
		xk, yk = x1*xk + n*y1*yk, x1*yk + y1*xk
