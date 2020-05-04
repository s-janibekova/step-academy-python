import sqlite3


def create_book_table():
  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()
  cursor.execute(f'CREATE TABLE IF NOT exists books(name text primary key, author text, read integer)')
  connection.commit()
  connection.close()



def add_book(name, author):
  # ",0);DROP TABLE books;"
  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()
  cursor.execute(f'INSERT INTO books VALUES(?, ? ,0)',(name, author))
  connection.commit()
  connection.close()


def get_all_books():
  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()
  cursor.execute(f'SELECT * FROM books')
  books = [ {'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
  connection.close()
  return books



def update_book(name):
  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()
  cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
  connection.commit()
  connection.close()



def delete_book(name):
  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()
  cursor.execute(f'DELETE FROM books WHERE name = ? ', (name,))
  connection.commit()
  connection.close()





