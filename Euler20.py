#!/usr/bin/env pypy
from operator import mul
print sum(int(c) for c in str(reduce(mul, xrange(1, 100))))

#ignore 100, only adds zeroes

'''
Alternatively

from Lib import merge, besieve, bemul

q = reduce(merge, besieve(100))
q[2] -= q[5]
q[5] = 0

print sum(int(c) for c in str(bemul(q)))

'''
