import os, sys
from time import time, sleep
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta 

def deco(func):
	def wrapper(arg):
		s = time()
		func(arg)
		print('{:.2f} sec'.format(time()-s))
	return wrapper

@deco
def func1(arg):
	sleep(arg)

if __name__ == "__main__":
	func1(5)
