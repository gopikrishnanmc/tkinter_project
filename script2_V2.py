import sqlite3
import pymysql

def create_table():
    conn = sqlite3.connect("lite2.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite2.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (? , ? , ?)",(item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite2.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = sqlite3.connect("lite2.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))
    conn.commit()
    conn.close()

#insert("Coffee cup", 10, 5)
#delete("Coffee cup")
update(11,6,"Wine Glass")
print(view())

