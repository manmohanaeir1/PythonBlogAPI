import psycopg2

from model.Blog import Blog

def deb_connect():
    return  psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost", port="5432")


def get_blogs():
    conn =  deb_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM BLOG")
    data = cur.fetchall()
    cur = conn.cursor()
    cur.close()

    blogs = [Blog(id=blog[0], title=blog[1], description=blog[2]) for blog in data]
    return blogs

def get_blog(id):
    conn =  deb_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM BLOG WHERE ID = %s", (id,))
    data = cur.fetchone()
    cur.close()

    if data:
        return  Blog(id=data[0], title=data[1], description=data[2])
    else:
        return None
    
    def create_blog(title, description):
        conn =  deb_connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO BLOG (TITLE, DESCRIPTION) VALUES (%s, %s)", (title, description))
        new_blog_id = cur.fetchone()[0]
        conn.commit()
        cur.close()

        return new_blog_id
    
    def update_blog(id, title, description):
        conn =  deb_connect()
        cur = conn.cursor()
        cur.execute("UPDATE BLOG SET TITLE = %s, DESCRIPTION = %s WHERE ID = %s", (title, description, id))
        conn.commit()
        cur.close()

    def delete_blog(id):
        conn =  deb_connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM BLOG WHERE ID = %s", (id,))
        conn.commit()
        cur.close()


    