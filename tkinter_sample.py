from tkinter import *

window = Tk()

def Kg_to():
    t1.delete("0.0",END)
    t1.insert(END, int(e1_value.get())*1000)
    t2.delete("0.0",END)
    t2.insert(END, int(e1_value.get())*2.20462)
    t3.delete("0.0",END)
    t3.insert(END, int(e1_value.get())*35.274)
    
b1 = Button(window, text="Convert", command=Kg_to)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2 = Label(window,text="Kg")
e2.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()





import sqlite3

def create_table():
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert_table(item,quantity,price):
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()
    
create_table()
insert_table("Biriyani", 1, 220.50)
insert_table("Grilled chicken", 1, 240.50)


def view_table():
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM store')
    data = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]
    print(data)
    print(cols)
    conn.commit()
    conn.close()

view_table()

def delete_table(item):
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM store where item = ?',(item,))
    conn.commit()
    conn.close()

delete_table("Grilled chicken")

def update_table(quantity,price,item):
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute('UPDATE store SET quantity=?, price=? WHERE item=?',(quantity,price,item,))
    conn.commit()
    conn.close()

update_table(11,2500.90,"Grilled chicken")














import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='Test_db_1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert_table(item,quantity,price):
    conn = psycopg2.connect("dbname='Test_db_1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()    

def view_table():
    conn = psycopg2.connect("dbname='Test_db_1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM store')
    data = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]
    print(data)
    print(cols)
    conn.commit()
    conn.close()

def delete_table(item):
    conn = psycopg2.connect("dbname='Test_db_1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM store where item = %s',(item,))
    conn.commit()
    conn.close()

def update_table(quantity,price,item):
    conn = psycopg2.connect("dbname='Test_db_1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s',(quantity,price,item,))
    conn.commit()
    conn.close()


create_table()
insert_table("Biriyani", 1, 220.50)
insert_table("Grilled chicken", 1, 240.50)
view_table()
delete_table("Grilled chicken")
update_table(11,2500.90,"Grilled chicken")
