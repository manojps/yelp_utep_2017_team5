import pandas as pd
import numpy as np
import psycopg2
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import precision_recall_fscore_support
import matplotlib.pyplot as plt

db_conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = db_conn.cursor()
#cur.execute("select u1.user_id, u1.review_count, u1.funny, u1.useful, u1.cool, u1.fans, u2.fashion, u2.fashion_lasvegas, u2.friend_count, u2.tips_count, u1.elite from _user as u1 join secondary_stats_1 as u2 on u1.user_id = u2.user_id limit 500;")
cur.execute("select u1.user_id, u1.review_count, u1.funny, u1.useful, u1.cool, u1.fans, u2.fashion, u2.friend_count, u2.tips_count, u2.city, u1.elite from _user as u1 join (select t1.user_id, t1.fashion, t1.friend_count, t1.tips_count, t2.city from secondary_stats_1 as t1 join user_location_temp as t2 on t1.user_id= t2.user_id where city like '%Phoenix%') as u2 on u1.user_id = u2.user_id;")

data = cur.fetchall()

df = pd.DataFrame(data)

df[10][df[10] != '{None}'] = 'Elite' # Labels. Change column index by updating the database query
df[10][df[10] == '{None}'] = 'Not elite' # Labels
df[6] = df[6].astype(int)
df.head()

# train, test = df[df['is_train']==True], df[df['is_train']==False]

# http://stackoverflow.com/questions/24147278/how-do-i-create-test-and-train-samples-from-one-dataframe-with-pandas
#msk = np.random.rand(len(df)) < 0.8
#train = df[msk]
#test = df[~msk]

train, test = train_test_split(df, test_size = 0.3)
print('Training samples', len(train))
print('Testing samples', len(test))
#del df['column_name']

#http://stackoverflow.com/questions/29221502/pandas-selecting-discontinuous-columns-from-a-dataframe
features = df.columns[1:9]
#features.head()
clf = RandomForestClassifier(n_jobs=6)
#y, _ = pd.factorize(train['species'])
#y = df[9]
#y = np.asarray(train[df[10]])
#y = train[10].values
y = pd.factorize(train[10])[0]
#y = np.asarray(train[a], dtype="bool")


clf.fit(train[features].values, y)

#preds = iris.target_names[clf.predict(test[features])]
pred = clf.predict(test[features])
print(pred)
label = pd.DataFrame(pred)
label[0][label[0] >= 0.5 ] = 1
label[0][label[0] < 0.5 ] = 0
label['user_id'] = df[0]
label['city'] = df[9]
print(label)

#print(label[0:1][0])
print(test[10].values)
#pd.crosstab(test[10], pred, rownames=['actual'], colnames=['pred'])

z = pd.factorize(test[10])[0]
ari = adjusted_rand_score(z, label[0].values)
print("ARI = ", ari)
# ari = adjusted_rand_score(test[10].values, label[0].values)
# print("ARI = ", ari)

print (sorted(zip(map(lambda x: round(x, 4), clf.feature_importances_), list(df.columns.values)), reverse=True))

data = sorted(zip(map(lambda x: round(x, 4), clf.feature_importances_), list(df.columns.values)), reverse=True)

x_val = [x[1] for x in data]
y_val = [x[0] for x in data]

print (x_val)
#plt.plot(x_val,y_val)
plt.figure()
plt.title("Feature importances")
plt.bar(x_val,y_val, color="r", align="center")
#plt.xticks(range(x_val), indices)
#plt.xlim([-1, x_val])
plt.show()

label.to_csv('rf_fashion_lasveags.csv', sep='\t')
test.to_csv('test.csv', sep='\t')

#prf = precision_recall_fscore_support(test[10].values, label[0].values)
#print("PRF\n", prf)

#pd.crosstab(test[df[5]], preds, rownames=['actual'], colnames=['preds'])
