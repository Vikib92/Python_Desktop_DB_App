import sqlite3

class Database():
    
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)" )
        self.conn.commit()
    
    def insert(self,title,author,year,isbn):
        self.cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        
    def view(self):
        self.cursor.execute("SELECT * FROM book")
        rows=self.cursor.fetchall()
        return rows
    
    def search(self,title="",author="",year="",isbn=""):
        self.cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR YEAR=? OR isbn=?",(title,author,year,isbn))
        rows=self.cursor.fetchall()
        return rows
    
    def delete(self,id):
        self.cursor.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
    
    def update(self,id,title,author,year,isbn):
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
    
#insert('Heart of the Ocean', 'Sam Boyle', 1975, 99874)
#insert('The Shining', 'R.L.Stine', 1963, 99634)
#insert('To kill a mocking bird', 'Tom clancy', 1938, 95274)
#view()