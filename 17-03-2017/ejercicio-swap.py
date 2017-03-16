#!/usr/bin/python
# coding: utf-8

c1 = 'a'
c2 = 'b'

ce = c2
c2 = c1
c1 = ce
del ce

print c1, c2 
