__author__ = 'santhosh'

import pandas
from utils import data_helper
import matplotlib.pyplot as plt

train_data, train_data_target, test_data, cols = data_helper.read_data()

for col in cols:
    print col
    data = train_data[col]
    print data[0]
    print(len(data))
    # if len(data) > 0:
    #     plt.title(col)
    #     plt.hist(data, bins=10)
    #     plt.show()

