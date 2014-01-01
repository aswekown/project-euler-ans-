#!/usr/bin/env python
#-*- coding:utf-8 -*-

# answer: 104743

alist = [2, 3]
def isornot(anum, a):
	for i in a:
		if anum % i == 0:
			return False
	a.append(anum)
	return True

for e in range(2, 10000000):
	isornot(e, alist)
	if len(alist) == 10001:
		break

print alist[5]
print alist[10000]
