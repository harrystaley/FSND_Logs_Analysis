#! /usr/bin/env python
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def top_articles():
    """
    FInds the top three articles and displays them in descending 
    order by article popularity as defined by the number of times an article
    has been visited.
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT title, COUNT(ip) AS visits " +
              "FROM article_log_view GROUP BY title " +
              "ORDER BY visits DESC LIMIT 3")
    DB.commit()
    articles = c.fetchall()
    DB.close()
    return articles


def top_authors():
    """
    queries the authors and displays them in descending
    order by popularityas defined by the number of times an article
    has been visited.
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT name, COUNT(ip) AS visits " +
              "FROM article_log_view GROUP BY name " +
              "ORDER BY visits DESC")
    DB.commit()
    authors = c.fetchall()
    DB.close()
    return authors


def top_error_rates():
    """
    Identifies what days had greater than 1% of errors occour based on
    http status codes.
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM error_rates_view WHERE rate >= 1")
    DB.commit()
    error_rates = c.fetchall()
    DB.close()
    return error_rates

# DISPLAY RESULTS OF QUERIES

articles = top_articles()
authors = top_authors()
errors = top_error_rates()

# TOP 3 ARTICLES
print "1. What are the most popular three articles of all time?"
print "NOTE: Based upon the number of times an article has been accessed.\n"
for article in articles:
    print article[0] + " -- " + str(article[1]) + " views"
print "\n"

# TOP AUTHORS
print "2. Who are the most popular article authors of all time? "
print "NOTE: Based upon the number of times an article has been accessed.\n"
for author in authors:
    print author[0] + " -- " + str(author[1]) + " views"
print "\n"

# HIG ERROR RATES
print "3. On which days did more than 1% of requests lead to errors?\n"
for error in errors:
    print error[0] + " -- " + str(error[1]) + "%"

