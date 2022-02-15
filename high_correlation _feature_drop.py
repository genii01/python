# https://www.projectpro.io/recipes/drop-out-highly-correlated-features-in-python
# high correlation feature drop 
import pandas as pd
import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target

df = pd.DataFrame(X)
print(df.head())

cor_matrix = df.corr().abs()
upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
print(upper_tri)
to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.95)]
print(); print(to_drop)

df1 = df.drop(df.columns[to_drop], axis=1)
print(); 
print(df1.head