# -*- coding: utf-8 -*-
"""Copy of Copy of ML -Breast Cancer Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/107yDQ3Kbo_cE-wSGFUv0eZ6r6B7L42xA
"""

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/ingledarshan/AIML-B2/main/data.csv")

df.head()

df.columns

df.info()

df['Unnamed: 32']

df = df.drop("Unnamed: 32", axis=1)

df.head()

df.columns

df.drop('id', axis=1, inplace=True)
# df = df.drop('id', axis=1)

df.columns

type(df.columns)

l = list(df.columns)
print(l)

features_mean = l[1:11]

features_se = l[11:21]

features_worst = l[21:]

print(features_mean)

print(features_mean)

print(features_worst)

df.head(2)

df['diagnosis'].unique()
# M= Malignant, B= Benign

sns.countplot(df['diagnosis'], label="Count",);

df['diagnosis'].value_counts()

df.shape

"""Explore the data"""

df.describe()
# summary of all the numeric columns

len(df.columns)

# Correlation Plot
corr = df.corr()
corr

corr.shape

plt.figure(figsize=(8,8))
sns.heatmap(corr);

df.head()

df['diagnosis'] = df['diagnosis'].map({'M':1, 'B':0})

df.head()

df['diagnosis'].unique()

X = df.drop('diagnosis', axis=1)
X.head()

y = df['diagnosis']
y.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

df.shape

X_train.shape

X_test.shape

y_train.shape

y_test.shape

X_train.head(1)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

X_train

"""Machine Learning Models

Logistic Regression
"""

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

y_pred

y_test

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

lr_acc = accuracy_score(y_test, y_pred)
print(lr_acc)

results = pd.DataFrame()
results

tempResults = pd.DataFrame({'Algorithm':['Logistic Regression Method'], 'Accuracy':[lr_acc]})
results = pd.concat( [results, tempResults] )
results = results[['Algorithm','Accuracy']]
results

"""Decision Tree Classifier"""

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

dtc_acc = accuracy_score(y_test, y_pred)
print(dtc_acc)

tempResults = pd.DataFrame({'Algorithm':['Decision tree Classifier Method'], 'Accuracy':[dtc_acc]})
results = pd.concat( [results, tempResults] )
results = results[['Algorithm','Accuracy']]
results

"""Random Forest Classifier"""

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)

y_pred = rfc.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

rfc_acc = accuracy_score(y_test, y_pred)
print(rfc_acc)

tempResults = pd.DataFrame({'Algorithm':['Random Forest Classifier Method'], 'Accuracy':[rfc_acc]})
results = pd.concat( [results, tempResults] )
results = results[['Algorithm','Accuracy']]
results

"""Suppot Vector Classifier"""

from sklearn import svm
svc = svm.SVC()
svc.fit(X_train,y_train)

y_pred = svc.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

svc_acc = accuracy_score(y_test, y_pred)
print(svc_acc)

tempResults = pd.DataFrame({'Algorithm':['Support Vector Classifier Method'], 'Accuracy':[svc_acc]})
results = pd.concat( [results, tempResults] )
results = results[['Algorithm','Accuracy']]
results