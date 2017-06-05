-- delete the DB if it exists
DROP DATABASE IF EXISTS news;
-- Create the tournament database
CREATE DATABASE news;
-- connect to the database
\c news
-- Run the file to populate the database.
\i newsdata.sql

CREATE OR REPLACE VIEW article_author_join_view AS
	SELECT name, title, slug
	FROM authors
	LEFT OUTER JOIN articles
	ON authors.id = articles.author; 

CREATE OR REPLACE VIEW article_log_view AS
	SELECT name, title, ip, status, time
	FROM article_author_join_view
	LEFT OUTER JOIN log
	ON log.path LIKE '%'||article_author_join_view.slug;

CREATE OR REPLACE VIEW errors_per_day_view AS
	SELECT date_trunc('day', time) AS date, 
	COUNT(status) AS status_count,
	SUM(CASE WHEN status LIKE '%404%' THEN 1 ELSE 0 END) AS errors
	FROM log
	GROUP BY date;

CREATE OR REPLACE VIEW error_rates_view AS
	SELECT TO_CHAR(date, 'MM/DD/YYYY') AS date,
	ROUND(errors::decimal / status_count::decimal * 100, 2) AS rate
	FROM errors_per_day_view
	GROUP BY date, errors, status_count
	ORDER BY rate DESC;
