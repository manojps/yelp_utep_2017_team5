# Parse user data in a Postgres database
# Version 1.0
# Author: Manoj Pravakar Saha
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

import psycopg2
import json

# Load the whole JSON file in memory
f = open('yelp_academic_dataset_tip.json', 'r')

# Initialize an empty list for temporarily holding JSON objects as list
data = []

# Append each line/JSON object in a list
for line in f:
	data.append(json.loads(line))

# Open a connection to the database
db_conn = psycopg2.connect("dbname='database_name' host='server_address' user='username' password='password'")

# Iteratively commit the data from the list in database
i=0
while i < len(data):
    cur = db_conn.cursor()
    cur.execute("insert into Tip (user_id, business_id, tip_text, tip_date, likes, type) values (%s, %s, %s, %s, %s, %s)", (data[i]['user_id'], data[i]['business_id'], data[i]['text'], data[i]['date'], data[i]['likes'], data[i]['type']))
    db_conn.commit()
    #print(i)
    i += 1


# Close database connection
db_conn.close()

# Close JSON file 
f.close()
