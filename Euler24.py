#!/usr/bin/env pypy
from Lib import factorial

def e24(L=10**6, D=10):
	L += 1
	digits = [str(c) for c in xrange(D)]
	ret = ''
	while digits:
		f = factorial(len(digits)-1)
		i = L/f
		ret += digits[i]
		#~ print L, f, i, digits[i], digits
		L %= f
		digits.remove(digits[i])

	return ret

print e24()
