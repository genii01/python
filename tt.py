import os,sys

def func1(arg):
	try:
		if int(arg) <10:
			print(arg)
	except Exception as e:
		print(e)

func1(sys.argv[1])
