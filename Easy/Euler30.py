#!/usr/bin/env pypy

#brute force

ret = -1
for a in xrange(10):
	for b in xrange(10):
		for c in xrange(10):
			for d in xrange(10):
				for e in xrange(10):
					for f in xrange(10):
						if int(''.join(map(str, (a,b,c,d,e,f)))) == sum(x**5 for x in (a,b,c,d,e,f)):
							ret += int(''.join(map(str, (a,b,c,d,e,f))))

print ret
