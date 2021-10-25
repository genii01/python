import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,10,size = (20,3)), columns = ['user','item','score'])

agg_dict = {
    'item' : ['count','min','max','mean'],
    'score' : ['count','min','max','mean']
}
df_group = df.groupby(by = ['user'])
res_df = df_group.agg(agg_dict)
print(res_df)
col_name_list = []
for i in res_df.columns:
  col_name_list.append(i[0]+'_'+i[1])
col_name_list
res_df.columns = col_name_list
print(res_df)
res_df.reset_index(inplace =True)
