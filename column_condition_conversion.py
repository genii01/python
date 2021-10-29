def label_num_conversion(x):
  if x == 'L':
    return -1
  if x == 'M':
    return 0
  if x == 'H':
    return 1
df['Class_value'] = df['Class'].apply(lambda x : label_num_conversion(x))
df['Class_value'] = df['Class'].map({'L':-1,'M':0,'H':11,})
