#!/usr/bin/python

def lacz(s1,s2):
	res = ""
	lr = 0
	for i in range (len(s1)):
		if s1[i] == s2[i]: res += s1[i]
		else: res += "_"; lr += 1
	#endfor
	if lr == 1 : return res
	else: return False
#enddef


if __name__ == "__main__":
	print(lacz("001", "000"))
	print(lacz("001", "001"))
	print(lacz("001", "011"))
	print(lacz("001", "111"))


#	for i,j in zip (s1, s2):
#		if i == j : res += i
#		else : res += "_"; lr += 1

