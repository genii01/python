import seaborn as sns
import matplotlib.pyplot as plt

num_columns = app_train.dtypes[app_train.dtypes != 'object'].index
cat_columns = app_train.dtypes[app_train.dtypes == 'object'].index

def show_hist_by_target(df, cols):
  cond_1 = (df['TARGET'] == 1)
  cond_0 = (df['TARGET'] == 0)
  for col in cols:
    fig, axs = plt.subplots(figsize = (12,4), nrows = 1, ncols = 3, squeeze = False)
    sns.boxplot(data = df, x = 'TARGET', y = col, ax = axs[0][0])
    sns.violinplot(data=df, x= 'TARGET', y= col, ax = axs[0][1])
    sns.distplot(df.loc[cond_1,[col]], ax = axs[0][2], bins = 25, label = 1, color = 'r')
    sns.distplot(df.loc[cond_0,[col]], ax = axs[0][2], bins = 25, label = 0, color = 'b')
    plt.legend()
    plt.show()

def show_count_by_target(df, columns):
    cond_1 = (df['TARGET'] == 1)
    cond_0 = (df['TARGET'] == 0)
    
    for column in columns:
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(18, 4), squeeze=False)
        # countplot을 이용하여 category값의 histogram 표현
        chart0 = sns.countplot(df[cond_0][column], ax=axs[0][0])
        # x축의 tick label들이 값 유형이 많으므로 45도로 회전하여 표현
        chart0.set_xticklabels(chart0.get_xticklabels(), rotation=45)
        chart1 = sns.countplot(df[cond_1][column], ax=axs[0][1])
        chart1.set_xticklabels(chart1.get_xticklabels(), rotation=45)
        plt.legend()
        plt.show()

        
show_count_by_target(app_train, cat_columns)

show_hist_by_target(app_train,num_columns)
