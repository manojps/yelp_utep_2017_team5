# Frequency table for review count/year for users

import psycopg2
import datetime

db_conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = db_conn.cursor()
cur.execute("select review_count, yelping_since, user_id from _user;")
data = cur.fetchall()

#print(len(data))
#print(data)

current_date = datetime.datetime.now().date()

#print (type(data), '\n', data,'\n')

review_frquency = []


for item in data:
    # Assumption is every user is still active
    days_active = (current_date - item[1]).days
    #months_active = int(days_active*30)
    reviews_per_day = item[0]/days_active
    reviews_per_month = reviews_per_day*30
    review_frquency.append(reviews_per_month)
    cur.execute("update secondary_stats_1 set set avg_review = %s where user_id = %s", (reviews_per_month, item[3]))
    conn.commit()



cur.close()
db_conn.close()
