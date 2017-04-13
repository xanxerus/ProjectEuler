#!/usr/bin/pypy
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

def era(n, m):
	arr = [0,0]+range(2,n+1)
	for x in arr:
		if x:
			if x >= m:
				yield x
			for y in xrange(x<<1, n+1, x):
				arr[y] = 0

def e381(L=10**8):
	ret = 0
	for p in era(L, 5):
		ret += (p-3) * MMI(8, p) % p

	return ret

print e381(10**8)
