import pandas as pd

class Numerical:
    def converted(self,column,value):
        df_train = pd.read_csv('numerical_data.csv')
        cat_data = pd.read_csv('loan_train.csv')
        num = df_train.loc[cat_data[cat_data[column]==value].index[0]][column]
        return num

