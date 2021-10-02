## default loggin
# import logging 

# def sum(a,b):
#     res = a+b
#     logging.info(f'{a} & {b} is inserted values')
#     return res

# res = sum(1,10)
# print(res)

## info level logging
# import logging

# logging.basicConfig(level=logging.INFO)
# def hap(a, b):
#     ret = a + b
#     logging.info(f"input: {a} {b}, output={ret}")
#     return ret

# result = hap(3, 4)

import logging

logging.basicConfig(filename="mylog.txt", level=logging.INFO)

def hap(a, b):
    ret = a + b
    logging.info(f"input: {a} {b}, output={ret}")
    return ret

result = hap(3, 4)