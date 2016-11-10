#!/usr/bin/env pypy
'''
Case h is odd
(h+1)x + (h-1)y = l

since h*l is even, and h is odd, l is even
Let l = 2w, h+1 = 2u
2ux + (2u-2)y = 2w
2ux + 2uy - 2y = 2w
2ux + 2uy = 2w + 2y
ux + uy = w + y

Since u | w + y, let y be the smallest that makes this true.
y = (u-w%u)%u

Let uk = w+y
ux + uy = uk
x + y = k
x = k - y

x is nonnegative when k >= y

########################################################################

Case h is even and l is even
(h+1)x + (h-1)y = l

let l = 2w
(h+1)x + (h-1)y = 2w

Euclid's algorithm:
h+1 = (h-1)(1) + 2
h-1 = 2*( (h-1)/2 ) + 0

Extended algorithm:
(h+1)(1) + (h-1)(-1) = 2
(h+1)(w) + (h-1)(-w) = 2w

so (w, -w) is a solution

It can be verified that
x = w + (h-1)r
y = (h+1)r - w

Let w = x + (h-1)r
The minimum x is then
x = w % (h-1)
r = (w-x) / (h-1)
y = (h+1)r - w

y is nonegative when (h+1)r >= w

########################################################################

Case h is even and l is odd
(h+1)x + (h-1)y = l

let 2u = h
(2u+1)x + (2u-1)y = l

Euclidean algorithm:
(2u+1) = (2u-1)(1) + 2
(2u-1) = 2(u-1) + 1

Extended algorithm:
1 = (2u-1) + (2)(1-u)
2 = (2u+1) + (2u-1)(-1)
1 = (2u-1) + ((2u+1) + (2u-1)(-1))(1-u)
1 = (2u-1) + (2u+1)(1-u) + (2u-1)(u-1)
1 = (2u-1)(u) + (2u+1)(1-u)

(2u+1)(1-u) + (2u-1)(u) = 1
(2u+1)(l-lu) + (2u-1)(lu) = l

so (l-lu, lu) is a solution

It can be verified that
x = l-lu + (2u-1)r
y = lu - (2u+1)r

let lu = (2u+1)r + y
The minimum y is then
y = lu % (2u+1)
r = (lu - y) / (2u+1)
x = l - lu + (2u-1)r

x is nonnegative when l + (2u-1)r >= lu
'''
from math import sqrt
from time import time
from Lib import hm

def t(h, l):
	if h&1:
		u, w = h+1>>1, l>>1
		y = (u-w%u)%u
		k = (w+y) / u
		return k >= y
	else:
		for l in xrange(l-1, l+2):
			if l&1:
				u = h>>1
				y = l*u % (h+1)
				r = (l*u - y) / (h+1)
				if l + (h-1)*r >= l*u:
					return True
			else:
				w = l>>1
				x = w % (h-1)
				r = (w-x) / (h-1)
				if (h+1)*r >= w:
					return True
		return False

def T(s, L=0):
	ret = 0
	arr = set()
	for x in xrange(1, 1+int(sqrt(s))):
		if s%x == 0:
			arr.add(x)
	
	a = len(arr)
	for x in arr:
		a -= 1
		if not t(x, s/x):
			ret += 1
		if L - ret > a:
			return -1
	
	return ret

def hsieve(n):
	arr = [0, 1] + [0]*(n-1)
	for x in xrange(2, n+1):
		if arr[x] == 0:
			arr[x] = 2
			for y in xrange(x<<1, n+1, x):
				if arr[y] == 0:
					arr[y] = x
		else:
			h = hm(x, arr[x])
			arr[x] = (1+h)*(arr[x / arr[x]**h])
	return arr

def e256(L=200, M=10**8):
	t = time()
	H = hsieve(M)
	print 'hsieve', time()-t

	for x in xrange(L**2-L&1, M+1, 2):
		if H[x] >= 2*L and T(x) == 200:
			return x

print e256()
