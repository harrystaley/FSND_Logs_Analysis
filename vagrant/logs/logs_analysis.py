import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def top_articles():
    """FInds the top three articles."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT title, COUNT(ip) AS visits " +
              "FROM article_log_view GROUP BY title " +
              "ORDER BY visits DESC LIMIT 3")
    DB.commit()
    articles = c.fetchall()
    DB.close()
    return articles

articles = top_articles()

print "1. What are the most popular three articles of all time? \n"
for article in articles:
    print article[0] + " -- " + str(article[1]) + " views"

print "\n"
