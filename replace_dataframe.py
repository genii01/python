import pandas as pd
import numpy as np 
import sys, os

df = pd.DataFrame({
                  'user' : list(range(5)),
                  'contents' : ['apple','apple melon','apple apple water','mango orange','orange apple']
                  })
df['contents'].str.replace('apple', 'grape')
df.loc[df['contents'].str.startswith('apple'),:]
df[df['contents'].str.startswith('apple')]
df['contents'].apply(lambda x: x.replace('apple','potato'))
