#!/usr/bin/env pypy

from math import pi, sqrt, asin
from itertools import count

R = 10000.
A0 = R*R*(1 - pi/4)

def quad(a, b, c):
	det = b*b - 4*a*c
	if det < 0:
		return None
	elif det == 0:
		return -b / (2*a)
	else:
		return (-b + sqrt(det)) / (2*a), (-b - sqrt(det)) / (2*a)

def integral(a, b):
	anti = lambda x: ( (x-R)*sqrt(2*R*x - x*x) - R*R*asin((R-x)/R) ) / 2
	return anti(b) - anti(a)

def A(n=2.0):
	q = quad(1 + pow(n, -2), -2*R*(1 + 1/n), R*R)
	#~ print q
	G = min(q)
	return (G*G) / (2*n) + R*(R-G) - integral(G, R)

def E(L):
	for n in count(2):
		a = A(float(n))
		#~ print n, a, a/A0
		if a/A0 < L:
			return n

print E(.1/100)
