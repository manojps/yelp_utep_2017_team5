

create table user_friends (user_id varchar(50), friend_user_id varchar(50));

select count(user_id) from user_friends;

select count(distinct user_id) from user_friends;

