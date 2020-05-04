from .database_connection import DatabaseConnection


def create_book_table():
  with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute(f'CREATE TABLE IF NOT exists books(name text primary key, author text, read integer)')



def add_book(name, author):
  # ",0);DROP TABLE books;"
  with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO books VALUES(?, ? ,0)',(name, author))


def get_all_books():
  with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM books')
    books = [ {'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
  return books



def update_book(name):
  with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))



def delete_book(name):
  with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM books WHERE name = ? ', (name,))




