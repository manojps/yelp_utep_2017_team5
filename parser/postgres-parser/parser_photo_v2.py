# Parse photo data in a Postgres database
# Version 1.0
# Author: Manoj Pravakar Saha

# Import Psycopg Postgres adapter for Python
import psycopg2

# Import Python's default JSON encoder and decoder
import json

# Open a connection to the database
db_conn = psycopg2.connect("dbname='yelp' host='localhost' user='manoj' password=''")

# Initialize an empty list for temporarily holding a JSON object


# Open a JSON file from the dataset and read data line-by-line iteratively
f = open('photo_id_to_business_id.json')
# Initialize an empty list for temporarily holding JSON objects as list
data = []

# Append each line/JSON object in a list
for line in f:
	data.append(json.loads(line))

# Iteratively commit the data from the list in database
i=0
while i < len(data[0]):
	cur = db_conn.cursor()
	cur.execute("insert into photos (photo_id, business_id, caption, photo_label) values (%s, %s, %s, %s)", (data[0][i]['photo_id'], data[0][i]['business_id'], data[0][i]['caption'], data[0][i]['label']))
	db_conn.commit()
    #print(i)
	i += 1

# Close database connection
cur.close()
db_conn.close()
