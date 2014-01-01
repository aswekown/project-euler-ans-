#!/usr/bin/env python
#-*- coding:utf-8 -*-

# answer : 200 375 425

for i in xrange(1, 1000/3):
	for j in xrange(i, 1000/2):
		c = 1000 - i -j
		if (c**2 == i**2 + j**2):
			print i,j,c
