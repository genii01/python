import os ,sys

if not os.path.exists('./tmp'):
	os.mkdir('tmp')

if os.listdir('./tmp'):
	print('file exist')
