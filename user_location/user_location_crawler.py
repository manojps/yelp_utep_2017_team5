# Author: Manoj Pravakar Saha
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

from lxml import html
import requests
import psycopg2
import json

conn = psycopg2.connect("dbname='database' host='host_address' user='username' password='password'")

with open('yelp_academic_dataset_user.json') as fileobject:
	for line in fileobject:
		data = json.loads(line)
		url = 'https://www.yelp.com/user_details?userid='+data['user_id']

		page = requests.get(url)
		tree =  html.fromstring(page.text)
		user_location = tree.xpath('//*[@class="user-location alternate"]/text()')
		location = user_location[0].split(', ')

		if (len(location)== 0):
			continue
		elif (len(location) < 2):
			location.append(location [0])
			location[0] = ''
		elif (len(location) > 2):
			location [0] = location[1]
			location[1] = location[2]

		cur = conn.cursor()
		cur.execute("insert into user_location (user_id, user_city, user_state_country) values (%s, %s, %s)", (data['user_id'], location[0], location[1]))
		conn.commit()

cur.close()
conn.close()
