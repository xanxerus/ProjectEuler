#!/usr/bin/env pypy

name = [ '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ten  = [ '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

ret = len('onethousand')
for x in range(1, 1000):
	s = ''
	s += name[x//100]
	if x//100 > 0:
		s += 'hundred'
		if x%100 != 0:
			s += 'and'
	if x%100 >= 20:
		s += ten[(x%100)//10] + name[x%10]
	else:
		s += name[x%100]
	
	ret += len(s)

print ret
