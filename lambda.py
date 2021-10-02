import os, sys

print(os.getcwd())
print(os.listdir())

func1 = lambda x : x**2
res = func1(3)
print(res)