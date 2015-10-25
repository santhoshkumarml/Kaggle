from sklearn.tree import DecisionTreeClassifier
from utils import data_helper

train_data, train_data_target, test_data, cols = data_helper.read_data()

train_data['Sex'] = [1 if row=='male' else 0 for row in train_data['Sex']]
test_data['Sex'] = [1 if row=='male' else 0 for row in test_data['Sex']]

cl = DecisionTreeClassifier()  
cl_t = cl.fit(train_data[['Sex', 'Pclass', 'Parch', 'SibSp']], train_data_target)
op = cl.predict(test_data[['Sex', 'Pclass', 'Parch', 'SibSp']])

output_file = '../decision_tree.csv'
data_helper.write_data(test_data, output_file, op)
