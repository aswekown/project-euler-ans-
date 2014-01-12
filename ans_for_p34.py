#!/usr/bin/env python
#-*- coding:utf-8 -*-

# answer is : 40730

def getone(num):
	res = 1
	if num == 0 or num == 1:
		return res
	
	for i in xrange(1, num + 1):
		res *= i
	return res

if __name__ == '__main__':
	for i in xrange(10000000 + 1, 144, -1):
		sumit = sum(map(getone, map(int, str(i))))
		if sumit == i:
			print i
