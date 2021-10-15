import os, sys
import numpy as np
import pandas as pd

from time import time, sleep
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
 
if __name__== "__main__":
	with open('test.txt', 'w') as f:
		for s in range(10):
			data = '{} th data inserted \n'.format(s)
			f.write(data)
		
	print('readline'+'-'*50)
	with open('test.txt', 'r') as f:
		while True: 
			line = f.readline()
			if not line:
				break
			print(line)

	print('read'+'-'*50)
	with open('test.txt', 'r') as f: 
		line = f.read()
		print(line)

	print('readlines'+'-'*50)
	with open('test.txt', 'r') as f: 
		line = f.readlines()
		print(line)


	print('readline & strip'+'*'*10)
	with open('test.txt', 'r') as f:
		while True: 
			line = f.readline()
			if not line:
				break
			print(line.strip())

	
	
