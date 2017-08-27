import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='111222' host='localhost' port='5432'")
    cur  = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='111222' host='localhost' port='5432'")
    cur = conn.cursor()
    #The technique below works but prone to sql injections
    #cur.execute("INSERT INTO store VALUES ('%s' ,'%s' ,'%s')" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES (%s ,%s ,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn  = psycopg2.connect("dbname='database1' user='postgres' password='111222' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn  = psycopg2.connect("dbname='database1' user='postgres' password='111222' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price,item):
    conn  = psycopg2.connect("dbname='database1' user='postgres' password='111222' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s", (quantity, price,item))
    conn.commit()
    conn.close()

create_table()
#insert("Pear", 3 , 12.5)
#delete("Apple")
update(18,11.5, 'Pear')
print(view())





