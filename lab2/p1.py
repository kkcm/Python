#!/usr/bin/python

from string import ascii_lowercase

def vary(expression):
 	ws = []
 	for var in expression:
 		if var in ascii_lowercase and var not in ws:
 			ws.append(var)
 	return sorted(set(ws))
 
#def main(s):
# 	VAR = string.ascii_lowercase()
# 	vary(VAR)
#	print(VAR)
# while True:
# 	w = input("s")
# 	print(check(w))

VAR = ascii_lowercase
OP = "&>|"

def check(wyr):
 	stan = True
 	for z in wyr:
 	 	if stan:
 	 		if z in VAR:
 	 			stan = False
 	 		elif z in ')'+OP:
 	 			return False
 	 	else:
 	 		if z in OP:
 	 			stan = True
 	 		elif z in '('+VAR:
 	 			return False
 	return True


if __name__=="__main__":

	w = " a > s | ( q & b ) "

	print(vary(w))
 	print(check(w))
 
