name = ['merona', 'gugucon']
price = [500, 1000]

# zip & dict

icecream  = dict(zip(name,price))
print(icecream)


for n, p in zip(name, price):
    print(n, p)

아이스크림1 = {"메로나": 500, "구구콘": 1000}

아이스크림2 = dict(메로나=500, 구구콘=1000)

아이스크림3 = dict([("메로나", 500), ("구구콘", 1000)])


