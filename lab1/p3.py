#!/usr/bin/python

from p2 import sp

for i in range(1,1000000):
	j = sp(i)
	k = sp(j)
	if i == k and i != j:
		print (i, j)
	#endif
#endfor
print("Koniec")