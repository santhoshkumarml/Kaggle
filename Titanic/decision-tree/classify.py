'''
Created on Feb 14, 2015

@author: santhosh
'''

import pandas
from sklearn.tree import DecisionTreeClassifier
import csv
train_data = pandas.read_csv('../train.csv')
train_data_target = train_data['Survived']
train_data = train_data.drop('Survived',axis=1)
test_data = pandas.read_csv('../test.csv')

cols = list(test_data.columns.values)
cols.remove('PassengerId')

cl = DecisionTreeClassifier()
train_data['Sex'] = [1 if row=='male' else 0 for row in train_data['Sex']]
test_data['Sex'] = [1 if row=='male' else 0 for row in test_data['Sex']]
  
cl.fit(train_data[['Sex', 'Pclass', 'Parch', 'SibSp']], train_data_target)
op = cl.predict(test_data[['Sex', 'Pclass', 'Parch', 'SibSp']])
test_data = test_data.drop(cols, axis=1)
test_data['Survived'] = op
test_data.info()
test_data.to_csv('../decision_tree.csv', index=False)
