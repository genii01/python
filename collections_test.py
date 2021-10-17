from collections import Counter

lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']

res = Counter(lst)

print(res)

print('-'*80)
print('dictionary')

tmp = {'가': 3, '나': 2, '다': 4}
res = Counter(tmp)
print(res)

tmp = ['apple','apple','melon','melon','apple','watermelon']
res = Counter(tmp)
print(res)

ranking_res = Counter(tmp).most_common()
print(ranking_res)

first_res = Counter(tmp).most_common(1)
print(first_res)