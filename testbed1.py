#!/usr/bin/python
def caller():
	execfile("test2.py")
	return 'done'

d = {'mihir': caller()}
x = 'mihir'
k = d[x]
print k 
