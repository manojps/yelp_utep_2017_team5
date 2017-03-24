# Parse friend's of users in a table
# Version 1.0
# Author: Manoj Pravakar Saha
# This work is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International License.

# Database table creation query
# create table user_friends(user_id varchar(50), friend_user_id varchar(50));


# Import Psycopg Postgres adapter for Python
import psycopg2

# Import Python's default JSON encoder and decoder
import json

# Open a connection to the database
db_conn = psycopg2.connect("dbname='database_name' host='host_address' user='username' password='password'")

# Initialize an empty list for temporarily holding a JSON object
data = []

# Open a JSON file from the dataset and read data line-by-line iteratively
with open('yelp_academic_dataset_user.json') as fileobject:
	for line in fileobject:
		data = json.loads(line)

		# Parse the JSON object in your database
		i=0
		while data['friends'] is not None and i<len(data['friends']):
			cur = db_conn.cursor()
			cur.execute("insert into user_friends (user_id, friend_user_id) values(%s, %s)", (data['user_id'], data['friends'][i]))
			db_conn.commit()
			#print(i)
			i += 1
		
# Close database connection
db_conn.close()
