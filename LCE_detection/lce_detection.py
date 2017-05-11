# Combine results of P(L), P(E) and P(C) into P(LCE)

import psycopg2  # For connecting to PostgreSQL database
import pandas as pd # Data analysis toolkit with flexible data structures
import numpy as np # Fundamental toolkit for scientific computation with N-dimensional array support
from sqlalchemy import create_engine
import datetime
import matplotlib.pyplot as plt

conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = conn.cursor()

# Fetch P(C) where C = Food category
query = "select user_id, food_authority_prob from food_prob_rf2;"
cur.execute(query)
data = cur.fetchall()
df_food = pd.DataFrame(data)
df_food.rename(columns={df_food.columns[0]: 'user_id', df_food.columns[1]: 'food_prob'}, inplace=True)
df_food.head()

# Fetch P(C) where C = Nightlife category
query = "select user_id, nightlife_authority_prob from nightlife_prob_rf2;"
cur.execute(query)
data = cur.fetchall()
df_nl = pd.DataFrame(data)
df_nl.rename(columns={df_nl.columns[0]: 'user_id', df_nl.columns[1]: 'nightlife_prob'}, inplace=True)
df_nl.head()

# Fetch P(C) where C = Shopping category
query = "select user_id, shopping_authority_prob from shopping_prob_rf2;"
cur.execute(query)
data = cur.fetchall()
df_sp = pd.DataFrame(data)
df_sp.rename(columns={df_sp.columns[0]: 'user_id', df_sp.columns[1]: 'shopping_prob'}, inplace=True)
df_sp.head()

# Fetching P(E) data
query = "select user_id, elite_prob_rf from elite_prob_rf;"
cur.execute(query)
data = cur.fetchall()
df_e = pd.DataFrame(data)
df_e.rename(columns={df_e.columns[0]: 'user_id', df_e.columns[1]: 'elite_prob'}, inplace=True)
df_e.head()

# Fetch P(L) where L = Las Vegas
query = "select distinct user_id, probability from user_location_parallel where city like 'Las Vegas';"
cur.execute(query)
data = cur.fetchall()
df_lv = pd.DataFrame(data)
df_lv.rename(columns={df_lv.columns[0]: 'user_id', df_lv.columns[1]: 'lv_prob'}, inplace=True)
df_lv.head()

# Joining all the dataframes
df2 = pd.merge(df_e, df_lv, on='user_id', how='outer')
df3 = pd.merge(df2, df_food, on='user_id', how='outer')
df4 = pd.merge(df3, df_nl, on='user_id', how='outer')
df5 = pd.merge(df4, df_sp, on='user_id', how='outer')

# Calculating P(LCE) for Las Vegas food elite
df5['lv_food_elite'] = (df5['elite_prob']*df5['lv_prob']*df5['food_prob'])
# df5.sort(['lv_food_elite'], ascending=False)

# Calculating P(LCE) for Las Vegas nightlife elite
df5['lv_nl_elite'] = (df5['elite_prob']*df5['lv_prob']*df5['nightlife_prob'])
#df5.sort(['lv_nl_elite'], ascending=False)

# Calculating P(LCE) for Las Vegas shopping elite
df5['lv_sp_elite'] = (df5['elite_prob']*df5['lv_prob']*df5['shopping_prob'])
#df5.sort(['lv_sp_elite'], ascending=False)

# Write the data into database
engine = create_engine('postgresql://username:pass)(@server-ip:5432/yelp')
df5.to_sql('local_category_elite2', engine)

cur.close()
conn.close()
