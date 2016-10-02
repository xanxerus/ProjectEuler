#!/usr/bin/env pypy

def p(d):
	arr = []
	r = 1
	while True:
		r *= 10
		r %= d
		if r in arr:
			break
		arr.append(r)

	return len(arr) - arr.index(r)

def e26(L=1000):
	md, mv = 0, 0

	for x in xrange(2, L):
		q = p(x)
		if q>mv:
			md,mv=x,q
	return md

print e26()
