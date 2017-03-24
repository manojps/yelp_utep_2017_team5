# Author: Manoj Pravakar Saha
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

import psycopg2
import gmplot
db_conn = psycopg2.connect("dbname='database' host='host_address' user='username' password='password'")
cur = db_conn.cursor()
cur.execute("select latitude, longitude from business where postal_code='89109';")
lat_long = cur.fetchall()

latitude = []
longitude = [] 

for i in range(len(lat_long)):
	latitude.append(lat_long[i][0])
	longitude.append(lat_long[i][1])

gmap = gmplot.GoogleMapPlotter(36.1215,-115.1696, 13)
gmap.scatter(latitude, longitude, '#FF6666', edge_width=10)
gmap.draw('Code/yelp_local/map.html')

cur.close()
db_conn.close()





