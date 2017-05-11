# Script to classify nightlife experts

import psycopg2  # For connecting to PostgreSQL database
import pandas as pd # Data analysis toolkit with flexible data structures
import numpy as np # Fundamental toolkit for scientific computation with N-dimensional array support
from sklearn.mixture import GaussianMixture # Gaussian Mixutre Model in scikit-learn
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.naive_bayes import GaussianNB
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier

conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = conn.cursor()

# Fetch users review data
topic_authority = "select t1.user_id, count(distinct t1.review_id) as review_count, sum(t1.review_length) from (select bc.business_id, r.review_id, r.user_id, length(r.review_text) as review_length from business_category as bc join review as r on bc.business_id = r.business_id where bc.category like 'Nightlife' order by bc.business_id) as t1 group by t1.user_id order by review_count desc;"
cur.execute(topic_authority)
data = cur.fetchall()
df6 = pd.DataFrame(data)

df6.rename(columns={df6.columns[0]: 'user_id', df6.columns[1]: 'review_count', df6.columns[2]: 'review_length'}, inplace=True)

# calculate percetnage of businesses reviwed in the category and average review length
df6['reviewed_percentage'] = df6['review_count']*100/21189
df6['avg_review_len'] = df6['review_length']/df6['review_count']

# Classify topical authority according to certain criteria
df6['topic_authority'] = (df6['reviewed_percentage'] > 0.5) & (df6['avg_review_len'] > 560.23)

# Divide data for classification at 70:30 ratio
train, test = train_test_split(df6, test_size = 0.3)

# Train model
clf = RandomForestClassifier(n_jobs=8)
#clf = GaussianNB()
#clf = linear_model.LogisticRegression()

y = pd.factorize(train['topic_authority'])[0]
features = ['review_count', 'avg_review_len']
clf.fit(train[features], y)

# Test the model
df = pd.DataFrame(clf.predict_proba(test[features]))
temp = pd.DataFrame(clf.predict(test[features]))

df['topic_authority_label'] = temp[0]
df.rename(columns={df.columns[1]: 'nightlife_authority_prob'}, inplace=True)

# Calculate model accuracy
z = pd.factorize(test['topic_authority'])[0]
ari = adjusted_rand_score(z, df['topic_authority_label'].values)
print("ARI = ", ari)
