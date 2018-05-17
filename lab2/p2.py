#!/usr/bin/python
import string
from p1 import check

def parse(w):
	var = string.ascii_lowercase
	op = "&>|"
	st = True
	n = 0
	for z in w:
		if z == '(':
			n += 1
		if z == ')':
			n -= 1
		if n < 0:
			return False
		if st:
			if z in var:
				st = False
			elif z in ')' + op:
				return False
		else:
			if z in op:
				st = True
			elif z in '(' + var:
				return False
	if n != 0: 
		return False
	return not st

if __name__=="__main__":

	w = "a>s|(q&b)"

 	print(parse(w))
 	print(check(w))