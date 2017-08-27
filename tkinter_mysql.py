import pymysql
import sqlite3


def create_table():
    conn = pymysql.connect("localhost","db_test","111222","aliendatabase")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS store")
    sql = """CREATE TABLE store (
    item VARCHAR(20),
    quantity INT(20),
    price FLOAT(20)
    )"""
    cur.execute(sql)
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = pymysql.connect("localhost","db_test", "111222", "aliendatabase")
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def view():
    conn = pymysql.connect("localhost","db_test","111222","aliendatabase")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(item):
    conn = pymysql.connect("localhost","db_test","111222","aliendatabase")
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM store where item=%s",(item,))
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def update(quantity, price, item):
    conn = pymysql.connect("localhost","db_test","111222","aliendatabase")
    cur = conn.cursor()
    try:
        cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
        conn.commit()
    except:
        conn.rollback()
    conn.close()

#create_table()
#insert('Orange', 12, 15)
#delete("Coffee cup")
update(14, 6.5, "Orange")
print(view())

