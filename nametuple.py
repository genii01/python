from collections import namedtuple

Book = namedtuple('Book', ['title', 'price'])
mybook3 = Book("파이썬을 이용한 비트코인 자동매매", 27000)
print(mybook3.title, mybook3.price)

print('_'*80)
print(mybook3[0], mybook3[1])   # indexing
print('-'*80)
print(mybook3)

def show(title, price):
    print(title, price)

show(*mybook3)