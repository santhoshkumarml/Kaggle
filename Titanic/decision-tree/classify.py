from sklearn.tree import DecisionTreeClassifier
from utils import data_reader

train_data, train_data_target, test_data, cols = data_reader.read_data()

train_data['Sex'] = [1 if row=='male' else 0 for row in train_data['Sex']]
test_data['Sex'] = [1 if row=='male' else 0 for row in test_data['Sex']]

cl = DecisionTreeClassifier()  
cl_t = cl.fit(train_data[['Sex', 'Pclass', 'Parch', 'SibSp']], train_data_target)
op = cl.predict(test_data[['Sex', 'Pclass', 'Parch', 'SibSp']])

test_data = test_data.drop(cols, axis=1)
test_data['Survived'] = op
test_data.info()
test_data.to_csv('../decision_tree.csv', index=False)
