import pandas as pd
import numpy as np
import os,sys

df1 = pd.DataFrame(np.random.randint(1,10,size= (10,3)), columns = ['user','item','score'])
df2 = pd.DataFrame(np.random.randint(1,10,size= (10,3)), columns = ['user','item','score'])
df3 = pd.DataFrame(np.random.randint(1,10,size= (10,3)), columns = ['user','item','score'])

if not os.path.exists('data'):
	os.mkdir('data')

#
#df_list = [df1,df2,df3]
#for df in df_list:
#	df.to_csv(f'./data/{df}.csv')

df1.to_csv('./data/df1.csv', index = False)
df2.to_csv('./data/df2.csv', index = False)
df3.to_csv('./data/df3.csv', index = False)

print(os.listdir('./data/'))
df_list = []
for df in os.listdir('./data/'):
	df_tmp = pd.read_csv('./data/'+df)
	df_list.append(df_tmp)

total_df = pd.concat(df_list, axis =0)
total_df.reset_index(drop = True, inplace = True)
print(total_df)

