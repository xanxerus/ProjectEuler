#!/usr/bin/env pypy

M = 1000000007

def S(n):
  ret = 0
  q, r = divmod(n, 9)
  return pow(10, q, M) * ((r*(r+1)/2) + r + 6) - r - 6 - 9*q

print S(20)

def fib(n):
  ret = [0, 1]
  while len(ret) <= n:
    ret.append(ret[-1] + ret[-2])
  return ret

def e684(j):
  f = fib(j)
  ret = 0
  for i in range(2, j+1):
    print i, len(f)
    pot = S(f[i]) % M
    ret += pot
    ret %= M
    print '%s : %s : %s : %s' % (i, f[i], pot, ret)
  return ret

print e684(90)
