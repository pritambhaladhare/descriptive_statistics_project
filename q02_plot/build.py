# Default Imports
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
import numpy as np
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    mode = sale_price.mode()[0]
    plt.hist(sale_price, bins=10)
    plt.axvline(mean, label='mean', color='r')
    plt.axvline(median, label='median', color='g')
    plt.axvline(mode, label='mode', color='y')
    plt.legend()
    plt.show()
    return
