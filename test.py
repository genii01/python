# import sys
# from os.path import dirname
# from util import *
# print(sys.path)
# print(dirname('/Users/jy.choi/python'))
# print('-'*80)
# address()

from datetime import datetime
from dateutil.relativedelta import relativedelta
import warnings
import pickle
# --@TIME_LIMIT=60
warnings.filterwarnings('ignore')
date = datetime.today()
date_str = datetime.strftime(date, '%Y-%m-%d')
print(date_str)
print('-'*80)
final = date +relativedelta(days= 2)
print(datetime.strftime(final, '%Y-%m-%d'))