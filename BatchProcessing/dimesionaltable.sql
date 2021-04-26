-- INSERT DATA into TABLE
DELETE FROM dim_app_details;

USE users_app_db;
INSERT INTO users_app_batch_client_data
VALUES ('6', '2021-04-10', '385', 'Paper flowers instructions', 'ART_AND_DESIGN', 
'4.4', '167', '5.6M', '50,000+', 'Free', '0', 'Everyone', 'Art & Design', 'March 26, 2017', 
'1.0', '2.3 and up', '7378', 'Jasmine Willis', '21', 'Wisconsin', '130');


DROP TABLE IF EXISTS dim_user_details;
CREATE TABLE dim_user_details (user_key INT NOT NULL  PRIMARY KEY AUTO_INCREMENT) AS
SELECT DISTINCT user_id, user_name, user_age, user_location FROM users_app_batch_client_data
ORDER BY user_id ASC;
ALTER TABLE dim_user_details
RENAME COLUMN user_id TO user_id_;


DROP TABLE IF EXISTS dim_app_details;
CREATE TABLE dim_app_details (app_key INT NOT NULL  PRIMARY KEY AUTO_INCREMENT) AS
SELECT DISTINCT app_id, app, category, rating, reviews, app_size, installs, app_type, price, 
content_rating, genres, last_updated, current_version, android_version 
FROM users_app_batch_client_data
ORDER BY app_id ASC;
ALTER TABLE dim_app_details
RENAME COLUMN app_id TO app_id_;

DROP TABLE IF EXISTS dim_download_date;
CREATE TABLE dim_download_date (download_key INT NOT NULL  PRIMARY KEY AUTO_INCREMENT) AS
SELECT DISTINCT download_date FROM users_app_batch_client_data;
ALTER TABLE dim_download_date
RENAME COLUMN download_date TO download_date_;


DROP TABLE IF EXISTS fact_users_app_table;
CREATE TABLE fact_users_app_table (
user_key INT NOT NULL, app_key INT NOT NULL, user_id INT NOT NULL, app_id INT NOT NULL, 
 time_spent_min INT NOT NULL, download_date DATETIME);
-- fact_id INT NOT NULL  PRIMARY KEY AUTO_INCREMENT,

INSERT INTO fact_users_app_table
SELECT user_key, app_key, user_id, app_id, sum(time_spent_min), download_date_
FROM users_app_batch_client_data
JOIN dim_user_details ON user_id = user_id_
JOIN dim_app_details ON app_id = app_id_
JOIN dim_download_date ON download_date_ = download_date
GROUP BY user_key, app_key, user_id, app_id, download_date;

INSERT INTO dim_user_details(user_id_, user_name, user_age, user_location)
SELECT user_id, user_name, user_age, user_location FROM users_app_batch_client_data S
WHERE NOT EXISTS 
(SELECT * FROM dim_user_details U WHERE U.user_id_ = S.user_id AND
 U.user_name = S.user_name AND U.user_age = S.user_age AND U.user_location = S.user_location);

INSERT INTO dim_app_details (app_id_, app, category, rating, reviews, app_size, installs, app_type, price, 
content_rating, genres, last_updated, current_version, android_version)
SELECT app_id, app, category, rating, reviews, app_size, installs, app_type, price, 
content_rating, genres, last_updated, current_version, android_version FROM users_app_batch_client_data S
WHERE NOT EXISTS 
(SELECT * FROM dim_app_details A WHERE A.app_id_ = S.app_id AND A.app = S.app AND 
A.category = S.category AND A.rating = S.rating AND A.reviews = S.reviews AND
A.app_size = S.app_size AND A.installs = S.installs AND A.app_type = S.app_type AND A.price = S.price AND
A.content_rating = S.content_rating AND A.genres = S.genres AND A.last_updated = S.last_updated AND
A.current_version = S.current_version AND A.android_version = S.android_version);

INSERT INTO dim_download_date(download_date_)
SELECT download_date FROM users_app_batch_client_data S
WHERE NOT EXISTS
( SELECT * FROM dim_download_date D WHERE D.download_date_ = S.download_date);




INSERT INTO users_app_batch_client_data 
SELECT * 
FROM users_app_batch_client_data_temp

SELECT * FROM users_app_db.users_app_batch_client_data
WHERE user_id = 167;


DELETE FROM users_app_batch_client_data WHERE event_id > 100 AND event_id <= 10801;





ALTER TABLE dim_download_date ADD download_month VARCHAR NOT NULL;
 
UPDATE dim_download_date
SET download_month = download_date::CAST(DATE_FORMAT(download_date, '%M')) ; 

-- (dim_download_date_id INT NOT NULL  PRIMARY KEY AUTO_INCREMENT)

, datename(year,download_date) AS download_year, datename(month,download_date) AS download_month, 
datename(day,download_date) AS download_day
, CAST(DATE_FORMAT(download_date, '%M') AS DATE) as download_year

