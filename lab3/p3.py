#!/usr/bin/python

from string import ascii_lowercase
from open import open_K

def wypisz(s):
	mres = ""
	for w in s:
		res= ""
		for i,j in zip(w, ascii_lowercase[:len(w)]):
			if i == '0': res += "~"+j+"&"
			elif i == '1': res += j + "&"
		#endfor
		mres += "(" + res[:-1]+")"+"|"
	#endfor
	return mres[:-1]
#enddef

if __name__ == "__main__":
	dane = open_K("wektory.txt")
	print(wypisz(dane))
