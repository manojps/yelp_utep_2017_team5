# Parse check-ins in a Postgres database
# Version 1.0
# Author: Manoj Pravakar Saha
# This work is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International License.

# Import Psycopg Postgres adapter for Python
import psycopg2

# Import Python's default JSON encoder and decoder
import json

# Open a connection to the database
db_conn = psycopg2.connect("dbname='database_name' host='server_address' user='username' password='password'")

# Initialize an empty list for temporarily holding a JSON object
data = []

# Open a JSON file from the dataset and read data line-by-line iteratively
with open('yelp_academic_dataset_checkin.json') as fileobject:
	for line in fileobject:
		data = json.loads(line)
		
		# Segregate check-in time into hours and minutes
		i=0
		while i<len(data['time']):
			if data['time'][i][5] == ':':
				hour = data['time'][i][4]
				minute = data['time'][i][6:]
			else:
				hour = data['time'][i][4:6]
				minute = data['time'][i][7:]
			
			# Commit the data in database
			cur = db_conn.cursor()
			cur.execute("insert into checkin_extended (checkin_day, checkin_hour, checkin_minute, business_id, type) values(%s, %s, %s, %s, %s)", (data['time'][i][:3], hour, minute, data['business_id'], data['type']))
			db_conn.commit()
			
			i += 1
		
# Close database connection
db_conn.close()
