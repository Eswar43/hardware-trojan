# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 18:01:20 2021

@author: Eswar
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
path = r'C:\studies\project phase1\review\NETLIST\c432seqf.csv'
headernames = ['pi', 'po', 'lvls', 'conn', 'tp', 'label']
dataset = pd.read_csv(path, names = headernames)
print(dataset, "\n")
dataset.head()
X = dataset.iloc[1:, :-1].values
print(X,"\n")
y = dataset.iloc[1:, 5].values
print(y,"\n")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.70)
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 50)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(y_test,"\n")
print(y_pred,"\n")
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)
tp = result[0][0]
fp = result[0][1]
fn = result[1][0]
tn = result[1][1]
tpr = (tp)/(tp + fn)
print("Recall = ",tpr*100,"%")
tnr = (tn)/(tn + fp)
print("tnr = ",tnr*100,"%")
p = (tp)/(tp + fp)
print("Precision = ",p*100,"%")
f = (2 * p * tpr)/(p + tpr)
print("F-measure = ",f*100,"%")
a = (tp + tn)/(tp + fn + fp + tn)
print("Accuracy = ",a)
result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)
result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)
