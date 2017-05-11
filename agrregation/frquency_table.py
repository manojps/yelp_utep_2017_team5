# Frequenct table for review count

import psycopg2

db_conn = psycopg2.connect("dbname='yelp' host='' user='' password=''")
cur = db_conn.cursor()
cur.execute("select review_count from _user;")
review_count = cur.fetchall()

frequency = []

for i in range(0,121):
    frequency.append(0)

for review in review_count:
    count = (review[0]//100)
    frequency[count] = frequency[count] + 1

print(frequency)

cur.close()
db_conn.close()
