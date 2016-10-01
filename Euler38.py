#!/usr/bin/env pypy

from Lib import ordperm

def e38():
	for e in ordperm('987654321'):
		o = e
		for i in xrange(1, len(e)/2+1):
			e = o
			q = e[:i]
			w = int(q)

			while e.startswith(q):
				q, e = str(int(q)+w), e[len(q):]
			
			if not e:
				return o

print e38()

'''
mildly smart. 
take the front few characters, double them, and see if they match
the next few characters, repeating until the string is used up
'''
