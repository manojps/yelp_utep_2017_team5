import psycopg2
import gmplot
db_conn = psycopg2.connect("dbname='yelp' host='' user='manoj' password=''")
cur = db_conn.cursor()
#query = "select bb.latitude, bb.longitude from (select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_nl_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Nightlife' group by t2.business_id, t2.category order by c desc) as t3 join business as bb on t3.business_id=bb.business_id where t3.c>=20"
#query = "select bb.latitude, bb.longitude from (select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_food_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Food' group by t2.business_id, t2.category order by c desc) as t3 join business as bb on t3.business_id=bb.business_id where t3.c>=10"

query = "select bb.latitude, bb.longitude from (select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_sp_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Shopping' group by t2.business_id, t2.category order by c desc) as t3 join business as bb on t3.business_id=bb.business_id where t3.c>=5"

cur.execute(query)
lat_long = cur.fetchall()

latitude = []
longitude = []

for i in range(len(lat_long)):
	latitude.append(lat_long[i][0])
	longitude.append(lat_long[i][1])

gmap = gmplot.GoogleMapPlotter(36.1215,-115.1696, 13)
gmap.scatter(latitude, longitude, '#FF6666', edge_width=10)
gmap.draw('shopping_elite_business_map.html')

cur.close()
db_conn.close()
