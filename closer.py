import os, sys

def outer(num):
	def inner():
		print(num)
	return inner

f1 = outer(3)
f2 = outer(5)

print(f1())

print(f2())



