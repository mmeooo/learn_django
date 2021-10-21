import sqlite3
connect = sqlite3.connect('../db.sqlite3')

import pandas as pd
df = pd.read_sql_query('select * from members where age >= 25', connect )

df1 = pd.read_sql_query('select * from polls_economics where title like "%마스크%"', connect)
df2 = pd.read_sql_query('select * from polls_economics where title like "%노동%"', connect)
df3 = pd.read_sql_query('select * from polls_economics where title like "%소득%"', connect)


connect.close()

