#!/usr/bin/env python
#-*- coding:utf-8 -*-

# answer 6857

import math

def isornot(num):
	end = int(math.sqrt(num))
	for i in xrange(2, end + 1):
		if num % i == 0:
			return False
	return True


def answer(num):
	end = int(math.sqrt(num))
	for i in xrange(2, end + 1):
		if num % i == 0:
			yield i


print max(filter(isornot, answer(13195)))
