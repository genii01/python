import numpy as np
import pandas as pd

from time import time, sleep
from datetime import datetime

def deco(func):
	def inner(arg):
		s = time()
		func(arg)
		print('time = {:.2f} sec'.format(time()-s))
	return inner


@deco
def test(arg):
	print('function start')
	sleep(arg)

#test(4)
if __name__ == "__main__":
	test(4)

