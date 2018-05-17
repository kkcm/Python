#!/usr/bin/python

def open_K(file):
	f = open(file)
	dane = set(f.read().split())
	f.close
	return dane


if __name__ == "__main__":
	print(open_K("wektory.txt"))
#	dane = redukuj (dane)
#	print dane