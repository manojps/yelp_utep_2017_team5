# Parse user data in a Postgres database
# Version 1.0
# Author: Manoj Pravakar Saha
# This work is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International License.

import psycopg2
import json

# Load the whole JSON file in memory
#f = open('yelp_academic_dataset_tip.json', 'r')

# Initialize an empty list for temporarily holding JSON objects as list
data = []

# Open a connection to the database
db_conn = psycopg2.connect("dbname='database_name' host='server_address' user='username' password='password'")

# Iteratively commit the data from the list in database
with open('yelp_academic_dataset_tip.json') as fileobject:
    for line in fileobject:
        data = json.loads(line)
        cur = db_conn.cursor()
        cur.execute("insert into Tip (user_id, business_id, tip_text, tip_date, likes, type) values (%s, %s, %s, %s, %s, %s)", (data['user_id'], data['business_id'], data['text'], data['date'], data['likes'], data['type']))
        db_conn.commit()



# Close database connection
db_conn.close()

