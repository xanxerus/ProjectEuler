#!/usr/bin/env pypy

def linear_g(L):
  a = 1 # pow(2, x-3)
  b = 1 # G[x-1]
  c = 0 # sum(G[:-2])
  d = 0 # G[x-2]

  for x in xrange(3, L):
    a, b, c, d = a*2, a+b+c, c+d, b

  # return G[L] and sum(G[:L+1]) and G[L-1]
  return a+b+c, c + d + b + a+b+c, b

def pot_t(L):
  k = L>>1
  if not L&1: #even
    g_k, s_g, g_1 = linear_g(k+1)
    return g_k
  else: # odd
    g_k, s_g, g_1 = linear_g(k)
    return s_g

def g_clearer(L):
  f = 1 # pow(2, x-3)
  a = 0 # sum(G[:-2])
  b = 0 # G[x-2]
  c = 1 # G[x-1]

  for x in xrange(3, L):
    # progression
    f, a, b, c = f*2, a+b, c, f+a+c

  return f+a+c

from itertools import count

def e710(M=1000000, goal=0):
  f = 1 # pow(2, x-3)
  a = 0 # sum(G up to x-4)
  b = 0 # G[x-2]
  c = 1 # G[x-1]

  for k in count(3):
    # progression
    f, a, b, c = f*2%M, (a+b)%M, c, (f+a+c)%M
    
    if k < 42:
      continue

    # c is G[k]
    if a == goal:
      return 2*(k-2)+1
    elif c == goal:
      return 2*(k-1)

print e710()

