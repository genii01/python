import os, sys

class func: 
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __call__(self):
		print(self.a)
		print(self.b)

f1 = func(3,4)
f2 = func(5,6)
f1()
f2()
