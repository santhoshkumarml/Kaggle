from sklearn.linear_model import LogisticRegression
from utils import data_helper
import pandas

def format_data(data):
    data['Sex'] = [1 if row == 'male' else 0 for row in data['Sex']]
    data['Parch0'] = [1 if row == 0 else 0 for row in data['Parch']]
    data['Parch1'] = [1 if row == 1 else 0 for row in data['Parch']]
    data['Parch2'] = [1 if row == 2 else 0 for row in data['Parch']]
    data['Parch3'] = [1 if row == 3 else 0 for row in data['Parch']]
    data['Parch4'] = [1 if row == 4 else 0 for row in data['Parch']]
    data['Parch5'] = [1 if row == 5 else 0 for row in data['Parch']]
    data['Parch8'] = [1 if row == 8 else 0 for row in data['Parch']]
    data['SibSp0'] = [1 if row == 0 else 0 for row in data['SibSp']]
    data['SibSp1'] = [1 if row == 1 else 0 for row in data['SibSp']]
    data['SibSp2'] = [1 if row == 2 else 0 for row in data['SibSp']]
    data['SibSp3'] = [1 if row == 3 else 0 for row in data['SibSp']]
    data['SibSp4'] = [1 if row == 4 else 0 for row in data['SibSp']]
    data['SibSp5'] = [1 if row == 5 else 0 for row in data['SibSp']]
    data['SibSp6'] = [1 if row == 6 else 0 for row in data['SibSp']]
    data['EmbarkedQ'] = [1 if row == 'Q' else 0 for row in data['Embarked']]
    data['EmbarkedS'] = [1 if row == 'S' else 0 for row in data['Embarked']]
    data['EmbarkedC'] = [1 if row == 'C' else 0 for row in data['Embarked']]
    drop_cols = ['Name', 'Cabin', 'Ticket', 'Parch', 'SibSp', 'Embarked', 'Pclass', 'Age']
    data = data.drop(drop_cols, axis=1)
    return data

def classify():
    train_data, train_data_target, test_data = data_helper.read_data()
    train_data = format_data(train_data)
    train_data = train_data.drop(['PassengerId'], axis=1)
    train_data.info()
    test_data = format_data(test_data)
    l_r = LogisticRegression()
    l_r.fit(train_data, train_data_target)
    pred_test_data = test_data.drop(['PassengerId'], axis=1)
    print pandas.isnull(pred_test_data).any(1).nonzero()[0]
    op = l_r.predict(pred_test_data)
    output_file = '../logistic_regression.csv'
    data_helper.write_data(test_data, output_file, op)

if __name__ == '__main__':
    classify()

