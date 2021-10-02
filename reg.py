import re

text = "파이썬 좋아요. 파이썬은 누가 만들었나요?"
m = re.findall("파이썬", text)
print(m)


text = "파이썬/자바/C++"
m = re.split('/', text)
print(m)

date = "2020/06/30"
m = re.sub("/", "-", date)
print(m)