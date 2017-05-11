# Crawls Yelp website to fetch user location data and stores the information in a local database

from lxml import html
import requests
import psycopg2
import json
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
#app = open('user_id_list.txt','r')
#app_link = app.readlines()
#total_apps = app_link.__len__()

conn = psycopg2.connect("dbname='yelp' host='localhost' user='' password=''")

with open('user_id_list.txt') as fileobject:
	for line in fileobject:
		#print(line)
		#print(type(line))
		url = 'https://www.yelp.com/user_details?userid='+line
		#print(url)
		#page = requests.get(url, headers=headers)
		#print (url, '\n', page.request.headers, '\n',page)
		try:
			req = urllib.request.Request(url=url,data=b'None',headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'})
			#page = urllib.request.urlopen(req)
			t = urllib.request.urlopen(req)
			print(t.read())
			page = html.parse(t)
			#print(page)
			# print(url_req, '\n',page_text)
			#tree =  html.fromstring(page.text)
			user_location = page.xpath('//*[@class="user-location alternate"]/text()')
			if (len(user_location)== 0):
				continue

			location = user_location[0].split(', ')
			if (len(location) < 2):
				location.append(location [0])
				location[0] = ''
			elif (len(location) > 2):
				#temp = location[0]
				location [0] = location[1]
				location[1] = location[2]
			#print(line, '\t', location)

			# print(data['user_id'], '\t', location)
			cur = conn.cursor()
			cur.execute("insert into user_location (user_id, user_city, user_state_country) values (%s, %s, %s)", (line.strip('\n'), location[0], location[1]))
			conn.commit()

		except urllib.error.HTTPError as e:
			error_message = e.read()
			print(error_message)
			continue



cur.close()
conn.close()


#Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36
#Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
