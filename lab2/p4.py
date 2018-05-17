#!/usr/bin/python

from string import ascii_lowercase
from p3 import onp
from p2 import parse

VAR = ascii_lowercase

def mapuj (wyr, zm, val):
	l = list(wyr)
	for i in range (len(l)):
		p = zm.find(l[i])
		if p >= 0 : l[i] = val[p]
	#endfor
	return "".join(l)
#enddef

def Or(a,b): return a or b
def And(a,b): return a and b
def Imp(a,b): return (not a) or b

def var(w):
	return "".join(sorted(set(w) & set(VAR)))

def value (wyr, val):
	zm = var (wyr)
	wyr = mapuj(wyr, zm, val)
	stos = []
	for z in wyr:
		if z in '01':
			stos.append(int(z))
		elif z == "&":
			stos.append(And(stos.pop(), stos.pop()))
		elif z == "|":
			stos.append(Or(stos.pop(), stos.pop()))
		elif z == ">":
			b = stos.pop()
			stos.append(Imp(stos.pop(), b))
	#endfor
	return stos.pop()
#enddef

def gen(n):
	for i in range (2**n):
		yield bin(i)[2:].rjust(n, "0")
	

# for val in gen(5)

#napisac tablice prawdy

if __name__=="__main__":

	while True:
		w = input("Podaj input> ")
		if parse(w):
			v = var(w)
			lines = gen(len(v))
			for l in lines:
				print(l, value(onp(w), l))
		else:
			print("error")


#	value("a>s|(q&b)", "34")
#endif




