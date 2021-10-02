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

import os, sys

class person:
	def __init__(self):
		print('re-born')

p1 = person()

import os, sys

class MyClass:
	count = 0
	
	def __init__(self):
		MyClass.count += 1
	
	def get_count(self):
		return MyClass.count

c1 = MyClass()
c2 = MyClass()
c3 = MyClass()
print(c3.get_count())
print(MyClass.count)
