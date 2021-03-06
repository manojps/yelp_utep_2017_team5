import pandas as pd
import numpy as np
import psycopg2
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics.cluster import adjusted_rand_score


db_conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = db_conn.cursor()
#cur.execute("select u1.user_id, u1.review_count, u1.funny, u1.useful, u1.cool, u1.fans, u2.nightlife, u2.nightlife_lasvegas, u2.friend_count, u2.tips_count, u1.elite from _user as u1 join secondary_stats_1 as u2 on u1.user_id = u2.user_id limit 500;")
cur.execute("select u1.user_id, u1.review_count, u1.funny, u1.useful, u1.cool, u1.fans, u2.nightlife, u2.nightlife_lasvegas, u2.friend_count, u2.tips_count, u1.elite from _user as u1 join secondary_stats_1 as u2 on u1.user_id = u2.user_id limit 500;")

data = cur.fetchall()

df = pd.DataFrame(data)

df[10][df[10] != '{None}'] = 1 # Labels. Change column index by updating the database query
df[10][df[10] == '{None}'] = 0 # Labels

df.head()

# train, test = df[df['is_train']==True], df[df['is_train']==False]

# http://stackoverflow.com/questions/24147278/how-do-i-create-test-and-train-samples-from-one-dataframe-with-pandas
#msk = np.random.rand(len(df)) < 0.8
#train = df[msk]
#test = df[~msk]

train, test = train_test_split(df, test_size = 0.2)
print('Training samples', len(train))
print('Testing samples', len(test))
#del df['column_name']

#http://stackoverflow.com/questions/29221502/pandas-selecting-discontinuous-columns-from-a-dataframe
features = df.columns[1:10]
#features.head()
clf = RandomForestRegressor(n_jobs=4)
#y, _ = pd.factorize(train['species'])
#y = df[9]
#y = np.asarray(train[df[10]])
y = train[10].values
#y = np.asarray(train[a], dtype="bool")


clf.fit(train[features].values, y)

#preds = iris.target_names[clf.predict(test[features])]
pred = clf.predict(test[features])
print(pred)
label = pd.DataFrame(pred)
label[0][label[0] >= 0.5 ] = 1
label[0][label[0] < 0.5 ] = 0
label['user_id'] = df[0]
print(label)

#print(label[0:1][0])
print(test[10].values)
#pd.crosstab(test[10], pred, rownames=['actual'], colnames=['pred'])

ari = adjusted_rand_score(test[10].values, label[0].values)
print("ARI = ", ari)

#pd.crosstab(test[df[5]], preds, rownames=['actual'], colnames=['preds'])
