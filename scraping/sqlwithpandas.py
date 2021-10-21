from sklearn import datasets
boston = datasets.load_boston()

import pandas as pd
df = pd.DataFrame(boston['data'], columns= boston['feature_names']) # 데이터프레임 생성, 컬럼명 지정

import sqlite3
connect = sqlite3.connect('../db.sqlite3') # db.sqlite3 파일과 연결
df.to_sql('boston_table', connect, if_exists='append') # 테이블을 자동 생성, if_exists='append'(계속 집어넣기 insert) or 'replace' 대체

print(df)

connect.close()
