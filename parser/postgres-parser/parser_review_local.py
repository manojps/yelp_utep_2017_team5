# Parse reviews in a database table
# Version 1.0
# Author: Manoj Pravakar Saha


# Import Psycopg Postgres adapter for Python
import psycopg2

# Import Python's default JSON encoder and decoder
import json

# Open a connection to the database
db_conn = psycopg2.connect("dbname='database_name' host='server_address' user='username' password='password'")

# Initialize an empty list for temporarily holding a JSON object
data = []

# Open a JSON file from the dataset and read data line-by-line iteratively
with open('yelp_academic_dataset_review.json') as fileobject:
	for line in fileobject:
		data = json.loads(line)

		# Parse the JSON object in your database
		cur = db_conn.cursor()
		cur.execute("insert into Review (review_id, user_id, business_id, stars, review_date, review_text, useful, funny, cool, type) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['review_id'], data['user_id'], data['business_id'], data['stars'],data['date'],data['text'], data['useful'], data['funny'], data['cool'], data['type']))
		db_conn.commit()
		print(data['review_id'])
