# Parse business categories each business is listed under into a Postgres database. If a business is listed under three different categories then the categories will be parsed into three different rows.
# Version 1.0
# Author: Manoj Pravakar Saha
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

# Import Psycopg Postgres adapter for Python
import psycopg2

# Import Python's default JSON encoder and decoder
import json

# Open a connection to the database
db_conn = psycopg2.connect("dbname='database_name' host='server_address' user='username' password='password'")

# Initialize an empty list for temporarily holding a JSON object
data = []

# Open a JSON file from the dataset and read data line-by-line iteratively
with open('yelp_academic_dataset_business.json') as fileobject:
	for line in fileobject:
		data = json.loads(line)

		# Parse the JSON object in your database
		i=0
		while data['categories'] is not None and i<len(data['categories']):
			cur = db_conn.cursor()
			cur.execute("insert into business_category (business_id, category) values(%s, %s)", (data['business_id'], data['categories'][i]))
			db_conn.commit()
			#print(data['business_id'])
			i += 1
		
# Close database connection
db_conn.close()
