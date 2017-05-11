import pandas as pd
import numpy as np
import psycopg2
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split



db_conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = db_conn.cursor()
cur.execute("select review_count, useful, funny, cool, fans, elite from _user limit 500;")
data = cur.fetchall()

df = pd.DataFrame(data)

df[5][df[5] != '{None}'] = 1 # Labels. Change column index by updating the database query
df[5][df[5] == '{None}'] = 0 # Labels

df.head()

# train, test = df[df['is_train']==True], df[df['is_train']==False]

# http://stackoverflow.com/questions/24147278/how-do-i-create-test-and-train-samples-from-one-dataframe-with-pandas
#msk = np.random.rand(len(df)) < 0.8
#train = df[msk]
#test = df[~msk]

train, test = train_test_split(df, test_size = 0.2)
len(train)
len(test)
#del df['column_name']

#http://stackoverflow.com/questions/29221502/pandas-selecting-discontinuous-columns-from-a-dataframe
features = df.columns[:4]
clf = RandomForestRegressor(n_jobs=2)
#y, _ = pd.factorize(train['species'])
#y = df[9]
y = np.asarray(train[df[5]])
y = train[5].values
y = np.asarray(train[a], dtype="bool")


clf.fit(train[features].values, y)

#preds = iris.target_names[clf.predict(test[features])]
pred = clf.predict(test[features])
#pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])

pd.crosstab(test[df[5]], preds, rownames=['actual'], colnames=['preds'])
