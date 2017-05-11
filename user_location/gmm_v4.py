# User location centroid calculations using GMM without parallel proccessing
import psycopg2  # For connecting to PostgreSQL database
import pandas as pd # Data analysis toolkit with flexible data structures
import numpy as np # Fundamental toolkit for scientific computation with N-dimensional array support
from sklearn.mixture import GaussianMixture # Gaussian Mixutre Model in scikit-learn
from sqlalchemy import create_engine

conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = conn.cursor()
cur.execute("select r.user_id, b.latitude, b.longitude, b.city from review as r join business as b on b.business_id = r.business_id order by user_id;")
data = cur.fetchall()

df = pd.DataFrame(data)
df.rename(columns={df.columns[0]: 'user_id', df.columns[1]: 'latitude', df.columns[2]: 'longitude',  df.columns[3]: 'city'}, inplace=True)

users = df.user_id.unique()

columns = ['user_id']
location = pd.DataFrame(columns=columns)
#columns2 = ['latitude', 'longitude']
#location2 = pd.DataFrame(columns=columns2)
col = ['user_id', 'latitide', 'longitude', 'probability']
loc_temp = pd.DataFrame(columns=col)

for user in users:
    test = df.loc[df['user_id'] == user]
    unique_city = test.city.unique()
    x = test
    r = test.columns[1:3]
    gmix = GaussianMixture(n_components=len(unique_city), covariance_type='full')
    gmix.fit(x[r].values)
    label = gmix.predict(x[r].values)
    a = pd.DataFrame(label)
    b = a[0].groupby(a[0]).count()
    c = pd.DataFrame(b)
    reviews = len(a.index)
    p = c/reviews
    for i in range(0, len(gmix.means_)):
        location.loc[i] = [user]
    columns2 = ['latitude', 'longitude']
    location2 = pd.DataFrame(data=gmix.means_, columns=columns2)
    #location2 = pd.DataFrame(data=gmix.means_)
    location2 ['user_id'] = location
    location2 ['probability'] = p
    loc_temp = loc_temp.append(location2, ignore_index=True)
    location = location[0:0]
    del location2

engine = create_engine('postgresql://username:pass)(@localhost:5432/yelp')
loc_temp.to_sql('user_location_temp3', engine)
