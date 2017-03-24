# Parse user data in a Postgres database
# Version 1.0
# Author: Manoj Pravakar Saha
# This work is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International License.

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
		#print(len(data['elite']), data['elite'])
		i = 0
#		if data['elite'] is None:
#			cur = db_conn.cursor()
#			cur.execute("insert into user_elite (user_id, elite_year) values (%s, %s)", (data['user_id'], None))
#			db_conn.commit()

		while i<len(data['elite']):
			#print(type(data['elite'][i]))
			if data['elite'][i] != "None":
				cur = db_conn.cursor()
				cur.execute("insert into user_elite (user_id, elite_year) values (%s, %s)", (data['user_id'], data['elite'][i]))	
				db_conn.commit()
			else:
				break

			i += 1

		# Commit the data in database

		#cur.execute("insert into _User (user_id, name, review_count, yelping_since, friends, useful, funny, cool, fans, elite, average_stars, compliment_hot, compliment_more, compliment_profile, compliment_cute, compliment_list, compliment_note, compliment_plain, compliment_cool, compliment_funny, compliment_writer, compliment_photos, type) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['user_id'], data['name'], data['review_count'], data['yelping_since'], data['friends'], data['useful'], data['funny'], data['cool'], data['fans'], data['elite'], data['average_stars'], data['compliment_hot'], data['compliment_more'], data['compliment_profile'], data['compliment_cute'], data['compliment_list'], data['compliment_note'], data['compliment_plain'], data['compliment_cool'], data['compliment_funny'], data['compliment_writer'], data['compliment_photos'], data['type']))
		#db_conn.commit()
		#print(data['user_id'])

# Close database connection
db_conn.close()
