# Frequency table for review count/year for users

import psycopg2
import datetime

db_conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = db_conn.cursor()
cur.execute("select review_count, yelping_since from _user;")
data = cur.fetchall()

#print(len(data))
#print(data)

current_date = datetime.datetime.now().date()

#print (type(data), '\n', data,'\n')

review_frquency = []


for item in data:
    # Assumption is every user is still active
    days_active = (current_date - item[1]).days
    reviews_per_day = item[0]/days_active
    reviews_per_year = reviews_per_day*365
    review_frquency.append(reviews_per_year)
    #print (item[1], '\t', days_active, '\t', item[0], '\t', reviews_per_year)

#print(review_frquency)

frequency = []

for i in range(0,200):
     frequency.append(0)

#print(frequency)


for review in review_frquency:
    #print (review)
    count = (review//10)
    #print(int(count))
    frequency[int(count)] = frequency[int(count)] + 1
#
print(frequency)


cur.close()
db_conn.close()
