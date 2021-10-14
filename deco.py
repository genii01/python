from time import time

def deco(func):
	def wrapper(*args):
		s= time()
		print(s)
		func(*args)
		print(time()-s)
	return wrapper
@deco
def inner(*args):
	print(*args)
	
inner(5,34,5)
