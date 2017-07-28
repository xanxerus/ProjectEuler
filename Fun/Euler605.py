#!/usr/bin/env pypy

L = 10**8
N = 10**8 + 7
R = pow(2, 10**8+7)
q = R*10006 + 99990001
w = pow(2, 99990000)
e = q*w
r = pow(2, 2*N) - pow(2, N+1) + 1
print (e%L) * (r%L) % L

#THEY WERE FRICKING COPRIME
