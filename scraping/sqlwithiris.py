from sklearn import datasets
iris= datasets.load_iris()

import pandas as pd
df= pd.DataFrame(iris['data'], columns= iris['feature_names'])

import sqlite3
connect = sqlite3.connect('../db.sqlite3')
df.to_sql('iris_table', connect, if_exists='append')

print(df)

connect.close()
