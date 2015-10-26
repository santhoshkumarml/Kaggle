__author__ = 'santhosh'

from utils import data_helper
import matplotlib.pyplot as plt
import numpy as np

train_data, train_data_target, test_data = data_helper.read_data()


train_data['Sex'] = [1 if row=='male' else 0 for row in train_data['Sex']]

train_data['Parch0'] = [1 if row==0 else 0 for row in train_data['Parch']]
train_data['Parch1'] = [1 if row==1 else 0 for row in train_data['Parch']]
train_data['Parch2'] = [1 if row==2 else 0 for row in train_data['Parch']]
train_data['Parch3'] = [1 if row==3 else 0 for row in train_data['Parch']]
train_data['Parch4'] = [1 if row==4 else 0 for row in train_data['Parch']]
train_data['Parch5'] = [1 if row==5 else 0 for row in train_data['Parch']]
train_data['Parch8'] = [1 if row==8 else 0 for row in train_data['Parch']]


train_data['SibSp0'] = [1 if row==0 else 0 for row in train_data['SibSp']]
train_data['SibSp1'] = [1 if row==1 else 0 for row in train_data['SibSp']]
train_data['SibSp2'] = [1 if row==2 else 0 for row in train_data['SibSp']]
train_data['SibSp3'] = [1 if row==3 else 0 for row in train_data['SibSp']]
train_data['SibSp4'] = [1 if row==4 else 0 for row in train_data['SibSp']]
train_data['SibSp5'] = [1 if row==5 else 0 for row in train_data['SibSp']]
train_data['SibSp6'] = [1 if row==6 else 0 for row in train_data['SibSp']]


train_data['EmbarkedQ'] = [1 if row=='Q' else 0 for row in train_data['Embarked']]
train_data['EmbarkedS'] = [1 if row=='S' else 0 for row in train_data['Embarked']]
train_data['EmbarkedC'] = [1 if row=='C' else 0 for row in train_data['Embarked']]


drop_cols = ['Name', 'PassengerId', 'Cabin', 'Ticket', 'Parch', 'SibSp', 'Embarked']

train_data = train_data.drop(drop_cols, axis=1)

print list(train_data.columns.values)

def print_pos_neg(col):
    print '----------------------------------------'
    print col
    data = train_data[col]
    positive_samples = []
    negative_samples = []
    for i in range(len(data)):
        if train_data_target[i] == 1:
            positive_samples.append(data[i])
        else:
            negative_samples.append(data[i])
    print 'positive_1', positive_samples.count(1)
    print 'positive_0', positive_samples.count(0)
    print 'negative_1', negative_samples.count(1)
    print 'negative_0', negative_samples.count(0)
    print '----------------------------------------'

for col in list(train_data.columns.values):
    if col not in ['Age', 'Pclass', 'Fare']:
        print_pos_neg(col)
    else:
        data = train_data[col]
        fig, ax = plt.subplots(1, 1)
        data.hist(ax)
        plt.show()

