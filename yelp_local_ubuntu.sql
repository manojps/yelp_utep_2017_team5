create table photos (
   photo_id varchar(50),
   business_id varchar(50),
   caption text,
   photo_label text);


CREATE TABLE public.business
(
  business_id character varying(50),
  name text,
  neighborhood text,
  address text,
  city character varying(50),
  state character varying(20),
  postal_code character varying(10),
  latitude double precision,
  longitude double precision,
  stars numeric(2,0),
  review_count integer,
  is_open integer,
  attributes text,
  categories text,
  hours text,
  type character varying(20)
);

CREATE TABLE public._user
(
  user_id character varying(50),
  name character varying(100),
  review_count integer,
  yelping_since date,
  friends text,
  useful integer,
  funny integer,
  cool integer,
  fans integer,
  elite text,
  average_stars numeric(2,0),
  compliment_hot integer,
  compliment_more integer,
  compliment_profile integer,
  compliment_cute integer,
  compliment_list integer,
  compliment_note integer,
  compliment_plain integer,
  compliment_cool integer,
  compliment_funny integer,
  compliment_writer integer,
  compliment_photos integer,
  type character varying(20)
);

CREATE TABLE public.business_category
(
  business_id character varying(50),
  category text
);

CREATE TABLE public.checkin_extended
(
  checkin_day character varying(3),
  checkin_hour integer,
  checkin_minute integer,
  checkin_time character varying(10),
  business_id character varying(50),
  type character varying(20)
);

CREATE TABLE public.review
(
  review_id character varying(50),
  user_id character varying(50),
  business_id character varying(50),
  stars numeric(2,0),
  review_date date,
  review_text text,
  useful integer,
  funny integer,
  cool integer,
  type character varying(20)
);

CREATE TABLE public.tip
(
  tip_text text,
  tip_date date,
  likes integer,
  business_id character varying(50),
  user_id character varying(50),
  type character varying(20)
);

CREATE TABLE public.user_elite
(
  user_id character varying(50),
  elite_year integer
);

CREATE TABLE public.user_friends
(
  user_id character varying(50),
  friend_user_id character varying(50)
);

CREATE TABLE user_location_estimate (
user_id varchar(50),
latitude double precision,
longitude double precision,
neighborhood text,
address text,
city character varying(50),
state character varying(20),
postal_code character varying(10)
);

CREATE TABLE user_location_estimate2 (
user_id varchar(50),
latitude double precision,
longitude double precision,
neighborhood text,
address text,
city character varying(50),
state character varying(20),
postal_code character varying(10)
);

select * from business limit 100

select city, postal_code, sum(review_count) as s from business group by city, postal_code order by s desc limit 100;

select latitude, longitude from business where postal_code='89109'


select count(business_id) from business

select * from business limit 100;
select * from business_category limit 100;
select * from _user limit 1000;
select * from tip limit 100;
select * from checkin_extended limit 100;
select * from user_friends limit 100;
select * from user_elite limit 100;
select * from review limit 100;

select count(user_id) from user_friends;
select count(review_id) from review;

CREATE TABLE public.review_test
(
  review_id character varying(50),
  user_id character varying(50),
  business_id character varying(50),
  stars numeric(2,0),
  review_date date,
  review_text text,
  useful integer,
  funny integer,
  cool integer,
  type character varying(20)
);

select count(review_id) from review_test;

CREATE TABLE user_location (
user_id varchar(50),
user_city varchar(50),
user_state_country varchar(50)
);

select * from user_location limit 100;

select count(user_id) from user_location;

select * from user_location where user_state_country='NV'

select * from user_location where user_city like'%Las Vegas%'

select r.user_id, r.business_id from review as r, (select business_id from business where city like '%Las Vegas%') as b where  r.business_id=b.business_id


select r.user_id, r.business_id
from review as r, (select business_id from business where postal_code='85006') as b 
where  r.business_id=b.business_id
group by r.user_id, r.business_id


select r.user_id, count(r.business_id) as c
from review as r, (select business_id from business where postal_code='89109') as b 
where  r.business_id=b.business_id
group by r.user_id
order by c desc

select r.user_id, b.postal_code, count(r.business_id) as c
from review as r, (select business_id, postal_code from business where city like '%Las Vegas%') as b 
where  r.business_id=b.business_id
group by r.user_id, b.postal_code
order by c desc

select r.user_id, count(r.user_id) as c
from review as r, (select business_id, postal_code from business where city like '%Las Vegas%' or city like '%Phoenix%') as b 
where  r.business_id=b.business_id
group by r.user_id
order by c desc

select t.user_id, t.c
from (select r.user_id, count(r.user_id) as c
from review as r, (select business_id, postal_code from business where city like '%Las Vegas%' or city like '%Phoenix%') as b 
where  r.business_id=b.business_id
group by r.user_id
order by c desc) as t
where t.c >= 50;


select distinct r.user_id
from review as r, (select business_id, postal_code from business where city like '%Las Vegas%' or city like '%Phoenix%') as b 
where  r.business_id=b.business_id
group by r.user_id

select r.user_id, count(r.business_id) as c
from review as r
group by r.user_id
order by c desc

/* Buinesses a particular user reviewed */
select r.user_id, r.business_id  
from review as r, (select business_id from business where business_id='0DI8Dt2PJp07XkVvIElIcQ' or business_id='LTlCaCGZE14GuaUXUGbamg') as b 
where  r.business_id=b.business_id
group by r.user_id, r.business_id

(select business_id from business where city like '%Las Vegas%') as b

"0DI8Dt2PJp07XkVvIElIcQ"
"LTlCaCGZE14GuaUXUGbamg"
select business_id from business where business_id='0DI8Dt2PJp07XkVvIElIcQ' or business_id='LTlCaCGZE14GuaUXUGbamg'

"M6K 1L4"
select business_id from business where postal_code='M4W 1B7'


select * from review limit 100;

select user_id, review_id, review_text, length(review_text), char_length(review_text) from review where user_id='0gpFaPgAeR78Cxeo9gd4KQ';


select * from user_location;

select u.user_id, u.review_count, ul.user_city, ul. user_state_country
from user_location as ul inner join _user as u 
on trim(u.user_id) = trim(ul.user_id)

--------------------
Get business locations a prticular has reviewed
select b.latitude, b.longitude
from business as b, (select business_id from review where user_id = 'HFECrzYDpgbS5EmTBtj2zQ') as r 
where b.business_id = r.business_id;

Get count of cities where the reviewed businesses are located by a particular user
select count(distinct b.city)
from business as b, (select business_id from review where user_id = 'rt3PC7WCgCKsoufmQJELfw') as r 
where b.business_id = r.business_id;

select b.business_id, b.latitude, b.longitude from business as b, (select business_id from review where user_id = '"+user[0]+"') as r where b.business_id = r.business_id;

select b.business_id, r.user_id, b.latitude, b.longitude from business as b join review as r on b.business_id = r.business_id order by business_id limit 100;

select b.business_id, r.user_id, b.latitude, b.longitude from review as r join business as b on b.business_id = r.business_id limit 100;



select * from user_location_estimate;


select count(user_id) from user_location_estimate2;

select count(user_id) from _user where review_count>= 10;
----------------------------------------
Business category aggregation
select * from business_category limit 100;
select * from business limit 100;

select c.category, sum(b.review_count) as s from business_category as c
join business as b on c.business_id = b.business_id
group by c.category 
order by s desc

---------------------------------------
alter table _user add column nightlife numeric(10,2);
alter table _user add column food numeric(10,2);
alter table _user add column fashion numeric(10,2);

create table secondary_stats_1 (
user_id varchar(50),
nightlife  numeric(10,2),
food numeric(10,2),
fashion numeric(10,2),
nightlife_lasvegas  numeric(10,2),
food_lasvegas numeric(10,2),
fashion_lasvegas numeric(10,2),
nightlife_phoenix  numeric(10,2),
food_phoenix numeric(10,2),
fashion_phoenix numeric(10,2),
avg_review double precision,
days_active int,
months_active int,
friend_count int,
tips_count int,
tips_nightlife int,
tips_food int,
tips_fashion int,
tips_nightlife_lasvegas int,
tips_food_lasvegas int,
tips_fashion_lasvegas int,
tips_nightlife_phoenix int,
tips_food_phoenix int,
tips_fashion_phoenix int,
avg_review_word_count numeric(10,2)
);

---------------------------------------------------------------------
USER LOCATION TEMP

create table user_location_temp (user_id varchar(50), latitude double precision, longitude double precision, city varchar(50), state varchar(20));
INSERT INTO user_location_temp (user_id) select user_id from _user;

update user_location_temp set latitude = ll.latitude 
from user_location_estimate2 as ll where user_location_temp.user_id = ll.user_id;

UPDATE user_location_temp 
SET latitude = 0
where latitude is NULL;

update user_location_temp set longitude = ll.longitude 
from user_location_estimate2 as ll where user_location_temp.user_id = ll.user_id;

UPDATE user_location_temp 
SET longitude = 0
where longitude is NULL;

select * from user_location_temp where latitude >= 36.0 and latitude<=37.0 order by latitude desc limit 100;

UPDATE user_location_temp 
SET city = 'Las Vegas'
where (latitude>= 36.0 and latitude <=37.0) and (longitude<=-115.0 and longitude>= -116.0);

UPDATE user_location_temp 
SET city = 'Phoenix'
where (latitude>= 33.0 and latitude <=34.5) and (longitude<=-111.0 and longitude>= -112.5);

UPDATE user_location_temp 
SET city = 'unknown'
where city is NULL;

---------------------------------------------------------------------
select * from secondary_stats_1 limit 100;

select * from secondary_stats_1 order by nightlife desc limit 100;

INSERT INTO secondary_stats_1 (user_id) select user_id from _user;

select bc.business_id, bc.category, r.user_id
from review as r join business_category as bc 
on r.business_id = bc.business_id 

select temp.user_id, temp.cnt
from (select t.user_id, count(t.user_id) as cnt
from (select bc.business_id, bc.category, r.user_id
from review as r join business_category as bc 
on r.business_id = bc.business_id) as t
where t.category like '%Nightlife%'
group by t.user_id
order by cnt desc) as temp

------------------------------------
reviews by each user in nightlife category

UPDATE secondary_stats_1 
SET nightlife = temp.cnt
from (select t.user_id, count(t.user_id) as cnt
from (select bc.business_id, bc.category, r.user_id
from review as r join business_category as bc 
on r.business_id = bc.business_id) as t
where t.category like '%Nightlife%'
group by t.user_id) as temp
where secondary_stats_1.user_id = temp.user_id

UPDATE secondary_stats_1 
SET nightlife = 0
where nightlife is NULL;

select user_id, nightlife from secondary_stats_1 order by nightlife desc
-----------------------------------

UPDATE secondary_stats_1 
SET food = temp.cnt
from (select t.user_id, count(t.user_id) as cnt
from (select bc.business_id, bc.category, r.user_id
from review as r join business_category as bc 
on r.business_id = bc.business_id) as t
where t.category like '%Restaurants%'
group by t.user_id) as temp
where secondary_stats_1.user_id = temp.user_id

UPDATE secondary_stats_1 
SET food = 0
where food is NULL;

select user_id, food from secondary_stats_1 order by food desc

---------------------------------
UPDATE secondary_stats_1 
SET fashion = temp.cnt
from (select t.user_id, count(t.user_id) as cnt
from (select bc.business_id, bc.category, r.user_id
from review as r join business_category as bc 
on r.business_id = bc.business_id) as t
where t.category like '%Shopping%'
group by t.user_id) as temp
where secondary_stats_1.user_id = temp.user_id

UPDATE secondary_stats_1 
SET fashion = 0
where fashion is NULL;

select user_id, fashion from secondary_stats_1 order by fashion desc

---------------------------------------------
reviews by each user in Nightlife category in a particular city

select t.user_id, count(t.user_id) as cnt
from (select bc.business_id, bc.category, r.user_id from review as r join business_category as bc on r.business_id = bc.business_id) as t
where t.category like '%Nightlife%'
group by t.user_id limit 100

UPDATE secondary_stats_1 
SET nightlife_lasvegas = temp.cnt
from (select t1.user_id, count(t1.user_id) as cnt
from (select t0.business_id, t0.city, t0.category, r.user_id from review as r join
(select bc1.business_id, bc1.category, b1.city from business_category as bc1 join business as b1 on bc1.business_id = b1.business_id) as t0 on r.business_id = t0.business_id) as t1
where t1.category like '%Nightlife%' and t1.city like '%Las Vegas%'
group by t1.user_id) as temp
where secondary_stats_1.user_id = temp.user_id


UPDATE secondary_stats_1 
SET nightlife_lasvegas = 0
where nightlife_lasvegas is NULL;

select user_id, nightlife, nightlife_lasvegas from secondary_stats_1 order by nightlife_lasvegas desc limit 1000;

------------------------------------------
UPDATE secondary_stats_1 
SET food_lasvegas = temp.cnt
from (select t1.user_id, count(t1.user_id) as cnt
from (select t0.business_id, t0.city, t0.category, r.user_id from review as r join
(select bc1.business_id, bc1.category, b1.city from business_category as bc1 join business as b1 on bc1.business_id = b1.business_id) as t0 on r.business_id = t0.business_id) as t1
where t1.category like '%Restaurants%' and t1.city like '%Las Vegas%'
group by t1.user_id) as temp
where secondary_stats_1.user_id = temp.user_id


UPDATE secondary_stats_1 
SET food_lasvegas = 0
where food_lasvegas is NULL;

select user_id, food, food_lasvegas from secondary_stats_1 order by food_lasvegas desc limit 1000;

--------------------------------------------
UPDATE secondary_stats_1 
SET fashion_lasvegas = temp.cnt
from (select t1.user_id, count(t1.user_id) as cnt
from (select t0.business_id, t0.city, t0.category, r.user_id from review as r join
(select bc1.business_id, bc1.category, b1.city from business_category as bc1 join business as b1 on bc1.business_id = b1.business_id) as t0 on r.business_id = t0.business_id) as t1
where t1.category like '%Shopping%' and t1.city like '%Las Vegas%'
group by t1.user_id) as temp
where secondary_stats_1.user_id = temp.user_id


UPDATE secondary_stats_1 
SET fashion_lasvegas = 0
where fashion_lasvegas is NULL;

select user_id, fashion, fashion_lasvegas from secondary_stats_1 order by food_lasvegas desc limit 1000;

----------------------------------------------
---------------------------------------------------
PHOENIX

UPDATE secondary_stats_1 
SET nightlife_phoenix = temp.cnt
from (select t1.user_id, count(t1.user_id) as cnt
from (select t0.business_id, t0.city, t0.category, r.user_id from review as r join
(select bc1.business_id, bc1.category, b1.city from business_category as bc1 join business as b1 on bc1.business_id = b1.business_id) as t0 on r.business_id = t0.business_id) as t1
where t1.category like '%Nightlife%' and t1.city like '%Phoenix%'
group by t1.user_id) as temp
where secondary_stats_1.user_id = temp.user_id


UPDATE secondary_stats_1 
SET nightlife_phoenix = 0
where nightlife_phoenix is NULL;

select user_id, nightlife, nightlife_phoenix from secondary_stats_1 order by nightlife_phoenix desc limit 1000;

------------------------------------------
UPDATE secondary_stats_1 
SET food_phoenix = temp.cnt
from (select t1.user_id, count(t1.user_id) as cnt
from (select t0.business_id, t0.city, t0.category, r.user_id from review as r join
(select bc1.business_id, bc1.category, b1.city from business_category as bc1 join business as b1 on bc1.business_id = b1.business_id) as t0 on r.business_id = t0.business_id) as t1
where t1.category like '%Restaurants%' and t1.city like '%Phoenix%'
group by t1.user_id) as temp
where secondary_stats_1.user_id = temp.user_id


UPDATE secondary_stats_1 
SET food_phoenix = 0
where food_phoenix is NULL;

select user_id, food, food_phoenix from secondary_stats_1 order by food_phoenix desc limit 1000;

--------------------------------------------
UPDATE secondary_stats_1 
SET fashion_phoenix = temp.cnt
from (select t1.user_id, count(t1.user_id) as cnt
from (select t0.business_id, t0.city, t0.category, r.user_id from review as r join
(select bc1.business_id, bc1.category, b1.city from business_category as bc1 join business as b1 on bc1.business_id = b1.business_id) as t0 on r.business_id = t0.business_id) as t1
where t1.category like '%Shopping%' and t1.city like '%Phoenix%'
group by t1.user_id) as temp
where secondary_stats_1.user_id = temp.user_id


UPDATE secondary_stats_1 
SET fashion_phoenix = 0
where fashion_phoenix is NULL;

select user_id, fashion, fashion_phoenix from secondary_stats_1 order by food_phoenix desc limit 1000;

-------------------------------------
select * from user_friends limit 100;
select user_id, count(user_id) as c from user_friends group by user_id order by  c desc limit 100;

UPDATE secondary_stats_1 
SET friend_count = temp.cnt
from (select user_id, count(user_id) as cnt from user_friends group by user_id) as temp 
where temp.user_id = secondary_stats_1.user_id;

UPDATE secondary_stats_1 
SET friend_count = 0
where friend_count is NULL;

select user_id, friend_count from secondary_stats_1 order by friend_count desc limit 100;
---------------------------------------


select user_id, review_count from _user order by review_count desc limit 100;

------------------------------------------
Tips aggregation

UPDATE secondary_stats_1 
SET tips_count = temp.cnt
from (select user_id, count(user_id) as cnt from tip group by user_id) as temp 
where temp.user_id = secondary_stats_1.user_id;

UPDATE secondary_stats_1 
SET tips_count = 0
where tips_count is NULL;

select user_id, tips_count from secondary_stats_1 order by tips_count desc limit 100;

-------------------------------------
select business_i

select * from tip limit 100;

select bc.business_id, bc.category, t.user_id
from tip as t join business_category as bc 
on t.business_id = bc.business_id limit 100;

---------------
tip for 

UPDATE secondary_stats_1 
SET tips_nightlife_lasvegas = temp.cnt
from (select t1.user_id, count(t1.user_id) as cnt
from (select t0.business_id, t0.city, t0.category, t.user_id from tip as t join
(select bc1.business_id, bc1.category, b1.city from business_category as bc1 join business as b1 on bc1.business_id = b1.business_id) as t0 on t.business_id = t0.business_id) as t1
where t1.category like '%Nightlife%' and t1.city like '%Las vegas%'
group by t1.user_id) as temp
where secondary_stats_1.user_id = temp.user_id

UPDATE secondary_stats_1 
SET tips_nightlife_lasvegas = 0
where tips_nightlife_lasvegas is NULL;

select * from secondary_stats_1 limit 100;

---------------------------------------------

select user_id, avg_review from secondary_stats_1 order by avg_review limit 100;

select count(user_id) from secondary_stats_1 where avg_review is not NULL;

select u1.user_id, u1.review_count, u1.funny, u1.useful, u1.cool, u1.fans, u2.nightlife, u2.friend_count, u2.tips_count, u2.nightlife_lasvegas, u1.elite
from _user as u1 join secondary_stats_1 as u2 on u1.user_id = u2.user_id limit 100;

select u1.user_id, u1.review_count, u1.funny, u1.useful, u1.cool, u1.fans, u2.nightlife, u2.friend_count, u2.tips_count, u2.city, u1.elite
from _user as u1 join 
(select t1.user_id, t1.nightlife, t1.friend_count, t1.tips_count, t2.city from secondary_stats_1 as t1 join user_location_temp as t2 on t1.user_id= t2.user_id where city like '%Las Vegas%') 
as u2
on u1.user_id = u2.user_id limit 100;


select * from photos limit 100;

select count(photo_id) from photos;

---------------------------------------
create table user_location_temp3 (user_id varchar(50), latitude double precision, longitude double precision, probability double precision, city varchar(50), state varchar(20));

select * from user_location_temp3 limit 100;

select r.user_id, b.latitude, b.longitude, b.city from review as r join business as b on b.business_id = r.business_id order by user_id limit 1000;


select * from user_location_parallel limit 100

--------------------------------------------
select t.user_id, t.c
from (select r.user_id, count(r.user_id) as c
from review as r, (select business_id, postal_code from business where state like '%NV%' or state like '%AZ%') as b 
where  r.business_id=b.business_id
group by r.user_id
order by c desc) as t
where t.c >= 50;

select r.user_id, b.latitude, b.longitude, b.city from review as r join business as b on r.business_id = b.business_id where r.user_id = '0A7vIgUb3Eazj21yzozbUg'


select distinct r.user_id from review as r, (select business_id, postal_code from business where state like '%NV%' or state like '%AZ%') as b where  r.business_id=b.business_id group by r.user_id


------------------------------------------------------
/* Business Category */
select * from business_category limit 100;

/* Businesses in a particular category */
select * from business_category where category like 'Nightlife';
select count(distinct business_id) from business_category where category like 'Shopping';

/* Number of businesses listed under different categories */
select category, count(distinct business_id) as business_count from business_category group by category order by business_count desc;

/* Review data */
select * from review limit 100;

/* All reviews in business category */
select bc.business_id, bc.category, r.review_id, r.user_id from business_category as bc join review as r on bc.business_id = r.business_id order by bc.business_id limit 1000;

/* All reviews in a particular category */
select t1.user_id, count(distinct t1.business_id) as review_count 
from (select bc.business_id, bc.category, r.review_id, r.user_id from business_category as bc join review as r on bc.business_id = r.business_id
where bc.category like 'Nightlife' order by bc.business_id) as t1 
group by t1.user_id order by review_count desc limit 10000;

/* Review count of each business from review table */
select business_id, count(review_id) as review_count from review group by business_id order by review_count desc limit 100;
select business_id, count(review_id) as review_count from review group by business_id order by business_id limit 100;

/*  */
select business_id from review where user_id = 'bLbSNkLggFnqwNNzzq-Ijw'

/*  */
select u1.user_id, u1.review_count, u1.funny, u1.useful, u1.cool, u1.fans, t1.friend_count, t1.tips_count, u1.elite 
from _user as u1 join secondary_stats_1 as t1 on u1.user_id= t1.user_id;

/*  */
select t1.user_id, count(distinct t1.review_id) as review_count, sum(t1.review_length)
from (select bc.business_id, r.review_id, r.user_id, length(r.review_text) as review_length 
from business_category as bc join review as r on bc.business_id = r.business_id where bc.category like 'Food' order by bc.business_id) as t1 
group by t1.user_id order by review_count desc limit 1000;

select t.user_id, count(t.review_id), sum(t.stars), sum(t.review_len) from (select user_id, review_id, stars, length(review_text) as review_len from review) as t group by t.user_id limit 100;

-===================
select * from elite_prob_rf limit 100;
select * from user_location_parallel limit 100;
select * from user_location_final limit 100;
select * from food_prob_rf limit 100;
select * from nightlife_prob_rf limit 100;
select * from shopping_prob_rf limit 100;

select distinct user_id from user_location_parallel where city like 'Las Vegas' limit 100;
select distinct user_id from user_location_parallel where city like 'Phoenix' limit 100;
select * from user_location_parallel where user_id like '002slNgnEtAvsNYFLw7rGA'


select distinct user_id, probability from user_location_parallel where city like 'Phoenix';

ALTER TABLE user_location_parallel ADD COLUMN city varchar(50);
ALTER TABLE user_location_parallel ADD COLUMN userid varchar(50);
---------------------------------------------------------------------
USER LOCATION TEMP

create table user_location_final (user_id varchar(50), latitude double precision, longitude double precision, probability double precision, neighborhood varchar(50), city varchar(50), state varchar(20));
INSERT INTO user_location_final (user_id) select user_id from _user;

update user_location_final set latitude = ll.latitude 
from user_location_parallel as ll where user_location_final.user_id = ll.user_id;

UPDATE user_location_final 
SET latitude = 0
where latitude is NULL;

update user_location_final set longitude = ll.longitude 
from user_location_parallel as ll where user_location_temp.user_id = ll.user_id;

UPDATE user_location_final 
SET longitude = 0
where longitude is NULL;

select * from user_location_parallel where latitude >= 36.0 and latitude<=37.0 order by latitude desc limit 100;

UPDATE user_location_parallel
SET city = 'Las Vegas'
where (latitude>= 36.0 and latitude <=37.0) and (longitude<=-115.0 and longitude>= -116.0);

UPDATE user_location_parallel 
SET city = 'Phoenix'
where (latitude>= 33.0 and latitude <=34.5) and (longitude<=-111.0 and longitude>= -112.5);

UPDATE user_location_parallel 
SET city = 'unknown'
where city is NULL;

---------------------------------------------------------------------
109 users
select user_id, lv_sp_elite, lv_nl_elite, lv_food_elite from local_category_elite2 where lv_sp_elite> 0order by lv_sp_elite desc;
590 users
select user_id, lv_sp_elite, lv_nl_elite, lv_food_elite from local_category_elite2 where lv_nl_elite>0  order by lv_nl_elite desc;
323 users
select user_id, lv_sp_elite, lv_nl_elite, lv_food_elite from local_category_elite2 where lv_food_elite> 0 order by lv_food_elite desc;

UPDATE local_category_elite2
SET lv_sp_elite = 0
where lv_sp_elite is NULL;

UPDATE local_category_elite2
SET lv_nl_elite = 0
where lv_nl_elite is NULL;

UPDATE local_category_elite
SET lv_food_elite = 0
where lv_food_elite is NULL


select count(user_id) from user_location_parallel
select count(user_id) from user_location_parallel where city like 'Las Vegas'

select * from local_category_elite2 limit 100;


select distinct user_id from local_category_elite2 where lv_sp_elite> 0
select distinct user_id from local_category_elite2 where lv_nl_elite> 0
select distinct user_id from local_category_elite2 where lv_food_elite> 0

Get business locations a prticular has reviewed
select b.latitude, b.longitude
from business as b, (select business_id from review where user_id = 'HFECrzYDpgbS5EmTBtj2zQ') as r 
where b.business_id = r.business_id;

Get count of cities where the reviewed businesses are located by a particular user
select count(distinct b.city)
from business as b, (select business_id from review where user_id = 'rt3PC7WCgCKsoufmQJELfw') as r 
where b.business_id = r.business_id;

select b.business_id, b.latitude, b.longitude from business as b, (select business_id from review where user_id = '"+user[0]+"') as r where b.business_id = r.business_id;

select b.business_id, r.user_id, b.latitude, b.longitude from business as b join review as r on b.business_id = r.business_id order by business_id limit 100;

select b.business_id, r.user_id, b.latitude, b.longitude from review as r join business as b on b.business_id = r.business_id limit 100;
==========================
select e.user_id, r.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_nl_elite> 0) as e join review as r on e.user_id=r.user_id

select e.user_id, r.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_sp_elite> 0) as e join review as r on e.user_id=r.user_id

select e.user_id, r.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_food_elite> 0) as e join review as r on e.user_id=r.user_id


select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_nl_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id

select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_food_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id

select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_sp_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id
--------------------------------
Nightlife
select t2.business_id, t2.name, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_nl_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Nightlife' group by t2.business_id, t2.category order by c desc

select t3.business_id, bb.name, t3.c
from (select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_nl_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Nightlife' group by t2.business_id, t2.category order by c desc) as t3
join business as bb on t3.business_id=bb.business_id


select t3.business_id, bb.latitude, bb.longitude
from (select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_nl_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Nightlife' group by t2.business_id, t2.category order by c desc) as t3
join business as bb on t3.business_id=bb.business_id where t3.c>=20


Food
select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category 
from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_food_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Food' group by t2.business_id, t2.category order by c desc

select t3.business_id, bb.name, t3.c
from (select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id 
from (select distinct user_id from local_category_elite2 as e where lv_food_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Food' group by t2.business_id, t2.category order by c desc) as t3
join business as bb on t3.business_id=bb.business_id

select t3.business_id, bb.latitude, bb.longitude
from(select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category 
from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_food_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Food' group by t2.business_id, t2.category order by c desc) as t3
join business as bb on t3.business_id=bb.business_id where t3.c>=10

Shopping
select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category 
from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_sp_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Shopping' group by t2.business_id, t2.category order by c desc

select t3.business_id, bb.name, t3.c
from (select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id 
from (select distinct user_id from local_category_elite2 as e where lv_sp_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Shopping' group by t2.business_id, t2.category order by c desc) as t3
join business as bb on t3.business_id=bb.business_id

select t3.business_id, bb.latitude, bb.longitude
from(select t2.business_id, t2.category, count(t2.business_id) as c from (select t1.user_id, t1.business_id, b.category 
from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_sp_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Shopping' group by t2.business_id, t2.category order by c desc) as t3
join business as bb on t3.business_id=bb.business_id where t3.c>=5

---------------------------
select t2.user_id, t2.business_id, t2.category from (select t1.user_id, t1.business_id, b.category from (select e.user_id, r.business_id from (select distinct user_id from local_category_elite2 as e where lv_nl_elite> 0) as e join review as r on e.user_id=r.user_id) as t1 
join business_category as b on t1.business_id=b.business_id) as t2 where t2.category like 'Nightlife'

select * from business limit 100
==========================

select e.user_id, u.user_id, u.review_count from (select distinct user_id from local_category_elite2 as e where lv_nl_elite> 0) as e join _user as u on u.user_id=e.user_id
