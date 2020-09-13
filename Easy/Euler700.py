#!/usr/bin/env pypy

from itertools import count

# modinverse function
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

# the coefficient and mod for this problem
A, M = 1504170715041707, 4503599627370517

# the point that we switch to constructing answers
cap = 111054189

# the running total
ret = A

# the last Euler coin we saw
prev = A

# narrow us down
for x in count(2):
  pot = A*x % M
  if pot < prev:
    prev = pot
    ret += pot
    if pot < cap:
      break

# get the narrow bit
Q = []
I = MMI(A, M)
for b in range(1, prev):
  # a number shows up at x=I*b, has value a*x%m
  # we toss it if there exists x'<x s.t. ax' < ax
  # Ax = b (mod m)
  x = I*b%M
  add = True
  remove = []

  # review the list
  for bp, xp in Q:
    if bp < b and xp < x:
      # this guy isn't getting added
      break
    elif b < bp and x < xp:
      # this guy is better than someone
      remove.append(xp)
  else:
    Q.append((b, x))
    for r in reversed(sorted(remove)):
      del Q[r]

B = sum(b for b, x in Q)
print B + ret
