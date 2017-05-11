import psycopg2
import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture



conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = conn.cursor()
cur.execute("select user_id from _user where review_count>= 10;")
data1 = cur.fetchall()


for user in data1:
    #print(user)
    #print(type(user))
    query1 = "select b.business_id, b.latitude, b.longitude from business as b, (select business_id from review where user_id = '"+user[0]+"') as r where b.business_id = r.business_id;"
    #query = "select count(b.business_id) from business as b, (select business_id from review where user_id = '"+user[0]+"') as r where b.business_id = r.business_id;"
    cur.execute(query1)
    data2 = cur.fetchall()
    df = pd.DataFrame(data2)
    #print(df)
    query2 = "select count(distinct b.city) from business as b, (select business_id from review where user_id = '"+user[0]+"') as r where b.business_id = r.business_id;"
    cur.execute(query2)
    data3 = cur.fetchall()
    n = data3[0][0]
    x = df
    r = df.columns[1:]
    x[r]
    gmix = GaussianMixture(n_components=n, covariance_type='full')
    gmix.fit(x[r].values)
    label = gmix.predict(x[r].values)
    a = pd.DataFrame(label)
    b = a[0].groupby(a[0]).count()
    c = pd.DataFrame(b)
    max_index = c[0].argmax()
    #print (user[0], '\t', gmix.means_)
    #print(type(gmix.means_))
    #print(user[0], '\t', n, '\t', max_index, '\t', gmix.means_[max_index][0], gmix.means_[max_index][1])
    #query2= "insert into _user_location_estimation (user_id, latitude, longitude) values (%s, %s, %s)", (user[0], gmix.means_[0][0], gmix.means_[0][1])
    cur.execute("insert into user_location_estimate2 (user_id, latitude, longitude) values (%s, %s, %s)", (user[0], gmix.means_[max_index][0], gmix.means_[max_index][1]))
    conn.commit()


#label = gmix.predict(df.values)
#a = pd.DataFrame(label)
#a[0].groupby(a[0]).count()

cur.close()
conn.close()
