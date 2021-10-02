from collections import Counter

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

res = Counter(z)

print(res)
print('-'*80)
print(res[0])
print('-'*80)
dic_conversion = dict(res)
print(type(res))
print('-'*80)
print(dic_conversion)
for idx, val in dic_conversion.items():
    print(idx, val)