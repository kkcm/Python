#!/usr/bin/python

from open import open_K
from p1 import lacz

def redukuj(dane):
	res = set()
	b2 = False

	for e1 in dane:
		b1 = False
		for e2 in dane:
			wym = lacz(e1,e2)
			if wym: res.add(wym); b1 = b2 = True
		#endfor
		if not b1: res.add(e1)
	#endfor
	if b2 : return redukuj(res)
	return res

if __name__ == "__main__":
	dane = open_K("wektory.txt")
	print(redukuj(dane))
