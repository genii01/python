class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price 

mybook = Book("파이썬을 이용한 비트코인 자동매매", 27000)
print(mybook.title, mybook.price)