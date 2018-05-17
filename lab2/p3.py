#!/usr/bin/python

from p1 import check

def bal(w, op):
	ln = 0
	for i in range (len(w)-1, 0, -1):
		if w[i] == '(' : ln += 1
		elif w[i] == ')' : ln -= 1
		if w[i] in op and ln == 0:
			return i
	#endfor
	return -1
#enddef

def onp(w):
	while w[0] == '(' and w[-1] == ')' and check(w[1:-1]):
		w = w[1:-1]
	p = bal (w, '>')
	if p >= 0:
		return onp(w[:p])+onp(w[p+1:])+w[p]
	
	p = bal (w, '|')
	if p >= 0:
		return onp(w[:p])+onp(w[p+1:])+w[p]
	
	p = bal (w, '&')
	if p >= 0:
		return onp(w[:p])+onp(w[p+1:])+w[p]
	return w
#enddef

def main():
	while True: 
		w = input()
		if check(w):
			print (onp(w))
		else: print("error")
		#endif

if __name__=="__main__":
	main()
#	w = "a>s|q&b"
#	print(bal("a>s|(q&b)", '|'))
#	print(onp(w))

