__author__ = 'santhosh'

from utils import data_helper
import matplotlib.pyplot as plt
import numpy as np


def format_data():
    train_data, train_data_target, test_data = data_helper.read_data()
    train_data['Sex'] = [1 if row == 'male' else 0 for row in train_data['Sex']]
    train_data['Parch0'] = [1 if row == 0 else 0 for row in train_data['Parch']]
    train_data['Parch1'] = [1 if row == 1 else 0 for row in train_data['Parch']]
    train_data['Parch2'] = [1 if row == 2 else 0 for row in train_data['Parch']]
    train_data['Parch3'] = [1 if row == 3 else 0 for row in train_data['Parch']]
    train_data['Parch4'] = [1 if row == 4 else 0 for row in train_data['Parch']]
    train_data['Parch5'] = [1 if row == 5 else 0 for row in train_data['Parch']]
    train_data['Parch8'] = [1 if row == 8 else 0 for row in train_data['Parch']]
    train_data['SibSp0'] = [1 if row == 0 else 0 for row in train_data['SibSp']]
    train_data['SibSp1'] = [1 if row == 1 else 0 for row in train_data['SibSp']]
    train_data['SibSp2'] = [1 if row == 2 else 0 for row in train_data['SibSp']]
    train_data['SibSp3'] = [1 if row == 3 else 0 for row in train_data['SibSp']]
    train_data['SibSp4'] = [1 if row == 4 else 0 for row in train_data['SibSp']]
    train_data['SibSp5'] = [1 if row == 5 else 0 for row in train_data['SibSp']]
    train_data['SibSp6'] = [1 if row == 6 else 0 for row in train_data['SibSp']]
    train_data['EmbarkedQ'] = [1 if row == 'Q' else 0 for row in train_data['Embarked']]
    train_data['EmbarkedS'] = [1 if row == 'S' else 0 for row in train_data['Embarked']]
    train_data['EmbarkedC'] = [1 if row == 'C' else 0 for row in train_data['Embarked']]
    drop_cols = ['Name', 'PassengerId', 'Cabin', 'Ticket', 'Parch', 'SibSp', 'Embarked']
    train_data = train_data.drop(drop_cols, axis=1)
    return train_data, train_data_target


def bar_binary_pos_neg(label):
    data = train_data[col]
    positive_samples = []
    negative_samples = []
    for i in range(len(data)):
        if train_data_target[i] == 1:
            positive_samples.append(data[i])
        else:
            negative_samples.append(data[i])

    index = np.arange(0, 2, 1)
    bar_width = 0.35

    fig = plt.figure()
    plt.title(label)
    rects1 = plt.bar(index,[positive_samples.count(0), positive_samples.count(1)], bar_width,
                 color='b',
                 label='Positive Samples')

    rects2 = plt.bar(index + bar_width, [negative_samples.count(0), negative_samples.count(1)], bar_width,
                 color='r',
                 label='NegativeSamples')

    plt.xlabel('Binary Label')
    plt.ylabel('Count')
    plt.xticks(index + bar_width)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plotHist(pos_data, neg_data, label):
    fig = plt.figure()
    plt.title(label)
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.hist(pos_data, color='b')
    ax2.hist(neg_data, color='r')
    plt.tight_layout()
    fig.show()

def hist_continuous_pos_neg(col):
    data = train_data[col]
    pos_data = [data[i] for i in range(len(data))if data[i] >=0 and train_data_target[i] == 1]
    neg_data = [data[i] for i in range(len(data))if data[i] >=0 and train_data_target[i] == 0]
    plotHist(pos_data, neg_data, col)

if __name__ == "__main__":
    train_data, train_data_target = format_data()
    for col in list(train_data.columns.values):
        if col not in ['Age', 'Pclass', 'Fare']:
            bar_binary_pos_neg(col)
        else:
            # pass
            hist_continuous_pos_neg(col)
