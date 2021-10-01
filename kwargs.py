def func(*args, **kwargs):
	print(args)
	print(kwargs)
res = list(range(10))
print('test1')
func(*res)

print('test2')
func(*res, a= 100, b=200)
