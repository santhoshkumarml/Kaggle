__author__ = 'santhosh'

import pandas

def read_data():
    train_data = pandas.read_csv('../train.csv')
    train_data_target = train_data['Survived']
    train_data = train_data.drop('Survived', axis=1)
    test_data = pandas.read_csv('../test.csv')
    cols = list(test_data.columns.values)
    cols.remove('PassengerId')
    return train_data, train_data_target, test_data, cols