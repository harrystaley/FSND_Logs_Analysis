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
