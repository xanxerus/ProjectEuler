#!/usr/bin/env pypy

from operator import mul

M = 1000000007

MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

def hm(y, x):
  ret = 0
  while y%x == 0:
    y /= x
    ret += 1
  return ret

def befactorize(n):
  A = [dict(), dict()] + range(2, n+1)
  for x in xrange(2, n+1):
    if isinstance(A[x], int):
      A[x] = {x: 1}
      for y in xrange(2*x, n+1, x):
        if isinstance(A[y], int):
          A[y] = {x: hm(y, x)}
        else:
          A[y][x] = hm(y, x)
  return A

def merge2(ret, b):
  for k, v in b.iteritems():
    ret[k] = ret.get(k, 0) + v
  return ret

def e650(N=20000):
  ret = 0
  f = befactorize(N)
  num = dict()
  den = dict()

  for n in xrange(1, N+1):
    #if n % 100 == 0:
    #  print n, len(num), len(den), max(num.values())
    # numerator (n!)
    merge2(num, f[n])
    # denominator (0! * 1! * 2! * ... * n!)
    merge2(den, num)
    # calculate sum of divisors
    s = 1
    for p, r_n in num.iteritems():
      # exponent is num * (n+1) - den * 2
      r = r_n * (n+1) - den[p] * 2
      # mod arithmetic for drastic speedup
      s *= (pow(p, r+1, M) - 1) * MMI(p-1, M) % M
    ret = (s + ret) % M
  return ret

from sys import argv
L = int(argv[1]) if len(argv) > 1 else 20000
#print L
print e650(L)
