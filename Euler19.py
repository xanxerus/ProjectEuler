#!/usr/bin/env pypy
from datetime import date, timedelta

d = date(1901, 1, 1)
while d.weekday() != 6:
	d += timedelta(1)

ret = 0
while d.year <= 2000:
	if d.day == 1:
		ret += 1
	d += timedelta(7)

print ret
