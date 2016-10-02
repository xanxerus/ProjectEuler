#!/usr/bin/env pypy

from Lib import era
from itertools import count

def e50(L=10**6):
	primes = era(L)
	bestrun = 1
	bestval = 0
	x = 0
	
	while x + bestrun <= len(primes):
		pot = sum(primes[x:x+bestrun])
		run = bestrun
		
		primepot = -1
		primerun = -1

		while x+run < len(primes) and pot < L:
			if pot in primes:
				primepot = pot
				primerun = run

			pot += primes[x+run]
			run += 1

		if primepot > 0:
			bestval = primepot
			bestrun = primerun

		x += 1

	return bestval

print e50()
#iterative sorta branch and bound?
