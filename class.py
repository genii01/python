import os, sys

class outer:
	def __init__(self, num):
		self.num = num
	def __call__(self):
		print(self.num)

f1 = outer(100)
f1()
