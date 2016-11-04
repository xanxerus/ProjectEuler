#!/usr/bin/env pypy

def e53(L=100, M=10**6):
	ret = 0
	last = [1]
	for n in xrange(1, L+1):
		curr = [1]
		for i in xrange(n-1):
			pot = last[i] + last[i+1]
			if pot > M:
				ret += 1
				pot = M
			curr.append(pot)
		curr.append(1)
		last = curr
	return ret

print e53()
