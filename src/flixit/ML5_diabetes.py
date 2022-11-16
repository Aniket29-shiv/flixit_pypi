# %% [markdown]
# # Assignment 5
# KNN algorithm on diabetes dataset

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

# %%
df=pd.read_csv('diabetes.csv')

# %%
df.columns

# %% [markdown]
# Check for null values. If present remove null values from the dataset

# %%
df.isnull().sum()

# %% [markdown]
# Outcome is the label/target, other columns are features

# %%
X = df.drop('Outcome',axis = 1)
y = df['Outcome']

# %%
from sklearn.preprocessing import scale
X = scale(X)
# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

# %%
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
 
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# %%
print("Confusion matrix: ")
cs = metrics.confusion_matrix(y_test,y_pred)
print(cs)

# %%
print("Acccuracy ",metrics.accuracy_score(y_test,y_pred))

# %% [markdown]
# Classification error rate: proportion of instances misclassified over the whole set of instances.
# Error rate is calculated as the total number of two incorrect predictions (FN + FP) divided by the total number of a dataset (examples in the dataset.
# 
# Also error_rate = 1- accuracy

# %%
total_misclassified = cs[0,1] + cs[1,0]
print(total_misclassified)
total_examples = cs[0,0]+cs[0,1]+cs[1,0]+cs[1,1]
print(total_examples)
print("Error rate",total_misclassified/total_examples)
print("Error rate ",1-metrics.accuracy_score(y_test,y_pred))

# %%
print("Precision score",metrics.precision_score(y_test,y_pred))

# %%
print("Recall score ",metrics.recall_score(y_test,y_pred))

# %%
print("Classification report ",metrics.classification_report(y_test,y_pred))


