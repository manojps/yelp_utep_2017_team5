# Script to classify elite users

import psycopg2  # For connecting to PostgreSQL database
import pandas as pd # Data analysis toolkit with flexible data structures
import numpy as np # Fundamental toolkit for scientific computation with N-dimensional array support
from sqlalchemy import create_engine
import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = conn.cursor()

# Fetch primary data and parse into a dataframe
cur.execute("select u1.user_id, u1.review_count, u1.funny, u1.useful, u1.cool, u1.fans, t1.friend_count, t1.tips_count, u1.elite from _user as u1 join secondary_stats_1 as t1 on u1.user_id= t1.user_id;")
data = cur.fetchall()
df_e = pd.DataFrame(data)

# Fetch secndary stats for users
cur.execute("select t.user_id, count(t.review_id), sum(t.stars), sum(t.review_len) from (select user_id, review_id, stars, length(review_text) as review_len from review) as t group by t.user_id;")
data = cur.fetchall()
df_rlen = pd.DataFrame(data)
df_rlen.head()

#Calculate average review length
df_rlen[4] = df_rlen[3]/df_rlen[1]
# Calculate average ratings
df_rlen[5] = df_rlen[2]/df_rlen[1]

# Rename 'user_id' column in both dataframes to prepare for join
df_e.rename(columns={df_e.columns[0]: 'user_id'}, inplace=True)
df_rlen.rename(columns={df_rlen.columns[0]: 'user_id'}, inplace=True)

# Join both dataframes with respect to 'user_id'
df_merge = pd.merge(df_e, df_rlen, on='user_id')
df_merge.head()

df_merge.rename(columns={df_merge.columns[0]: 'user_id', df_merge.columns[1]: 'review_count_2', df_merge.columns[2]: 'funny', df_merge.columns[3]: 'useful', df_merge.columns[4]: 'cool', df_merge.columns[5]: 'fans', df_merge.columns[6]: 'friend_count', df_merge.columns[7]: 'tips_count', df_merge.columns[8]: 'elite', df_merge.columns[9]: 'review_count', df_merge.columns[12]: 'avg_review_len', df_merge.columns[13]: 'avg_rating' }, inplace=True)

cur.execute("select user_id, yelping_since from _user;")
data = cur.fetchall()
user_age = pd.DataFrame(data)

current_date = datetime.datetime.now().date()
user_age['month_active'] = (current_date - user_age[1])/np.timedelta64(1, 'M')
user_age.rename(columns={user_age.columns[0]: 'user_id'}, inplace=True)

df_merge = pd.merge(df_merge, user_age, on='user_id')

# Conversting avergae review length to long review format
df_merge['avg_review_len'] = (df_merge['avg_review_len'] > 560.23)
df_merge['avg_review_len'] = df_merge['avg_review_len'].astype(int)

# Transform labels for 'elite' members
df_merge['elite'][df_merge['elite'] != '{None}'] = 'Elite' # Labels
df_merge['elite'][df_merge['elite'] == '{None}'] = 'Not elite' # Labels

# Spilitting data into training and test set
train, test = train_test_split(df_merge, test_size = 0.3)

# Initialize classificatio algorithm
clf = RandomForestClassifier(n_jobs=8)
#clf = GaussianNB()
#clf = linear_model.LogisticRegression()

y = pd.factorize(train['elite'])[0]
#features = ['review_count', 'avg_review_len', 'avg_rating','funny','useful','cool','fans','friend_count','tips_count' ]
features = ['review_count_2', 'avg_review_len', 'avg_rating','funny','useful','cool','friend_count','tips_count', 'fans', 'month_active']
clf.fit(train[features], y)

# Get prediction labels
temp = pd.DataFrame(clf.predict(test[features]))

# Get prediction probabilities
df_elite= pd.DataFrame(clf.predict_proba(test[features]))

# Assign prediction labels to df_elite datatframe
df_elite['elite_label'] = temp[0]

# Calculate user adjusted rand index
z = pd.factorize(test['elite'])[0]
ari = adjusted_rand_score(z, df_elite['elite_label'].values)
print("ARI = ", ari)

# Get feature improtance for Random Forest
print (sorted(zip(map(lambda x: round(x, 4), clf.feature_importances_), list(t.columns.values)), reverse=True))

cur.close()
conn.close()
