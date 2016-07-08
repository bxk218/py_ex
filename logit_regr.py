# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 15:54:40 2016

@author: Administrator
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X, y = iris.data[:-1, :], iris.target[:-1]
logistic = LogisticRegression()
logistic.fit(X,y)
print 'Predicted class %s, real class %s' % (logistic.predict(iris.data[-1,:]), iris.target[-1])
print 'Probabilities for each class from 0 to 2: %s' % logistic.predict_proba(iris.data[-1,:])
    

