#!/usr/bin/env python
#-*- coding:utf-8 -*-

# answer is 1533776805

T = set([(x*(x+1))/2 for x in xrange(1, 1000000)])
P = set([(x*(3*x-1))/2 for x in xrange(1, 1000000)])
H = set([(x*(2*x-1)) for x in xrange(1, 1000000)])

res = T & P & H



print res
