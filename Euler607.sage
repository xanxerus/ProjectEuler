#!/usr/bin/sage

from sage.numerical.optimize import minimize


#~ print 'Kitty'

q = 25*(sqrt(2) - 1)

#~ print q

a, b, c, d, e, f = var('a b c d e f')

w = q/(10*cos(a)) + 10/(9*cos(b)) + 10/(8*cos(c)) + 10/(7*cos(d)) + 10/(6*cos(e)) + 10/(5*cos(f)) + sqrt(q*q + (50*sqrt(2) - q*tan(a) - 10*(tan(b) + tan(c) + tan(d) + tan(e) + tan(f)))^2)/10

#~ print w

args = minimize(w, (pi/4,)*6)

#~ print args
print w(*args).n(digits=12)
