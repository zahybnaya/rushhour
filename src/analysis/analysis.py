import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from analyze_mags import MOVE_FILE_WITH_MAG

if __name__ == '__main__':
    """
    Example 
    """
    df = pd.read_csv(MOVE_FILE_WITH_MAG)

    sns.distplot(df.number_of_nodes)
    plt.show()

    sns.distplot(df.number_of_leaves)
    plt.show()


def lr_on_multiple_factors(df):
    sklearn.linear_model.LogisticRegression

