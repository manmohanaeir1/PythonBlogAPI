import psycopg2

conn =  psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("CREATE table IF NOT EXISTS BLOG (ID serial PRIMARY KEY, TITLE VARCHAR(100), DESCRIPTION VARCHAR(1000))")

cur.execute("INSERT INTO BLOG (TITLE, DESCRIPTION) VALUES ('First Blog', 'This is my first blog')")

conn.commit()
cur.close()
conn.close()
