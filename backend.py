import pymysql

def connect():
    conn = pymysql.connect("localhost","db_test","111222","test")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(20), author VARCHAR(20), year INT, ISBN INT)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = pymysql.connect("localhost","db_test","111222","test")
    cur = conn.cursor()
    cur.execute("INSERT INTO book values(NULL,%s, %s, %s, %s)",(title,author,year,isbn))
    conn.commit()
    conn.close()


def view():
    conn = pymysql.connect("localhost","db_test","111222","test")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = pymysql.connect("localhost","db_test","111222","test")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book where title=%s OR author=%s OR year =%s OR isbn=%s",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = pymysql.connect("localhost","db_test","111222","test")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id=%s",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = pymysql.connect("localhost","db_test","111222","test")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=%s, author=%s, year=%s,isbn=%s WHERE id=%s",(title,author,year,isbn,id))
    conn.commit()
    conn.close()




connect()
#insert("The Moon","John Day",1925,9167123)

#print(search(author="John Smooth"))
#delete(3)
#update(2,"The moon","John Smooth",1917,9973867)
#print(view())
