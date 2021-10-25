import os, sys 
import numpy as np
import pandas as pd

def add(a,b):
	'''
	add calculation
	'''
	assert type(a) == int
	assert type(b) == int
	return a+b

v1 = 3
print(type(v1))
v2 = 4
res = add(v1,v2)
print(res)
res =add (3.4,5)
print(res)
