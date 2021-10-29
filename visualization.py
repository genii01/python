def show_hist_by_target(df, cols):
  cond_h = (df['Class'] == 'H')
  cond_m = (df['Class'] == 'M')
  cond_l = (df['Class'] == 'L')

  for col in cols:
    fig, axs = plt.subplots(nrows = 1, ncols = 3, figsize = (14,7), squeeze = False)
    sns.set_palette('RdYlBu')
    sns.boxplot(data = df, x = 'Class', y = col, ax = axs[0][0])
    sns.violinplot(data = df, x = 'Class', y = col, ax = axs[0][1])
    sns.distplot(df[cond_h][col], bins = 50, ax = axs[0][2], label = 'H', color = 'red')
    sns.distplot(df[cond_m][col], bins = 50, ax = axs[0][2], label = 'M', color = 'orange')
    sns.distplot(df[cond_l][col], bins = 50, ax = axs[0][2], label = 'L', color = 'green')
    plt.title('{} - distplotting'.format(col))
    plt.show()

show_hist_by_target(df, num_cols)

def show_count_by_target(df, cols):
  cond_h = (df['Class'] == 'H')
  cond_m = (df['Class'] == 'M')
  cond_l = (df['Class'] == 'L')

  for col in cols:
    fig, axs = plt.subplots(figsize = (14,7), nrows =1, ncols = 3, squeeze = False)
    sns.set_palette('RdYlBu')
    chart_h = sns.countplot(df[cond_h][col], ax = axs[0][0], order = df[col].value_counts().index)
    chart_h.set_xticklabels(chart_h.get_xticklabels(), rotation = 45)
    chart_m = sns.countplot(df[cond_m][col], ax = axs[0][1], order = df[col].value_counts().index)
    chart_m.set_xticklabels(chart_m.get_xticklabels(), rotation = 45)
    chart_l = sns.countplot(df[cond_l][col], ax = axs[0][2], order = df[col].value_counts().index)
    chart_l.set_xticklabels(chart_l.get_xticklabels(), rotation = 45)
    plt.title('{}-count_plotting'.format(col))
    plt.legend()
    plt.show()

show_count_by_target(df, cat_cols)
