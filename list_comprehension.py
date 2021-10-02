import os, sys

# if 
res = [i**2 for i in range(10) if i >5 ]

print(res)

# if & else
res = [i**2 if i>4 else i for i in range(10)]
print('if & else : {}'.format(res))

# if & elif & else
res = [i**4 if i > 8 else i**2 if i >5 else i for i in range(10)]
print(res)


