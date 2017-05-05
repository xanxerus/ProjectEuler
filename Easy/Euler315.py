#!/usr/bin/env pypy

def numbits(n):
	ret = 0
	while n:
		if n&1:
			ret += 1
		n >>= 1
	return ret

def drs(n):
	while n > 9:
		yield n
		n = sum(map(int, str(n)))
	yield n
	yield 0

def era(n, start=0):
	arr = [0,0] + range(2,n+1)
	for x in arr:
		if x:
			if x >= start:
				yield x
			for y in xrange(x<<1, n+1, x):
				arr[y] = 0

def clock(n):
	ret = [0]*8
	x = 0
	while n:
		ret[x] = digits[n%10]
		n /= 10
		x += 1

	return ret

digits = [0b1111110, 0b1100000, 0b1011011, 0b1110011, 0b1100101, 0b0110111, 0b0111111, 0b1100110, 0b1111111, 0b1110111, 0]


def mux(a, b):
	ret = 0
	for x, y in zip(a, b):
		#~ print '\t', digits.index(x), digits.index(y), numbits(x) + numbits(y) - 2*numbits(x&y)
		ret += numbits(x) + numbits(y) - 2*numbits(x&y) 
	#~ print
	return ret

def sam(a):
	ret = 0
	for x in a:
		#~ print '\t', digits.index(x), numbits(x)
		ret += 2*numbits(x)
	return ret

def counts(n):
	m, s = 0, 0
	last = 0
	for x in drs(n):
		m += mux(clock(last), clock(x))
		s += sam(clock(x))
		#~ print x, mux(clock(last), clock(x)), sam(clock(x))
		last = x
	return s-m

ret = 0
for p in era(2*10**7, 10**7):
	ret += counts(p)

print ret

