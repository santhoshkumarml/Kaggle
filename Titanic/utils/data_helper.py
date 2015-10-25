__author__ = 'santhosh'

import pandas

def read_data():
    train_data = pandas.read_csv('../train.csv')
    train_data_target = train_data['Survived']
    train_data = train_data.drop('Survived', axis=1)
    test_data = pandas.read_csv('../test.csv')
    cols = list(test_data.columns.values)
    cols.remove('PassengerId')
    cols.remove('Name')
    return train_data, train_data_target, test_data, cols

def write_data(test_data, out_file, output):
    cols = list(test_data.columns.values)
    cols.remove('PassengerId')
    test_data = test_data.drop(cols, axis=1)
    test_data['Survived'] = output
    # test_data.info()
    test_data.to_csv(out_file, index=False)