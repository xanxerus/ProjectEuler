#!/usr/bin/env pypy

from Lib import besieve

def e29(L=100):
	ret = set()
	for a in besieve(L):
		if a:
			for b in xrange(2, L+1):
				ret.add(''.join('%d:%d\t' % (k, a[k]*b) for k in sorted(a.keys())))
	return len(ret)

print e29()
