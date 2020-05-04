from utils import database


USER_CHOICE = """
Enter:
'a' to add a new book
'l' to list all books
'r' to mark a book as read
'd' to delete a book
'q' to quit
Your choice: """





def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
          name = input("Enter the name of the book: ")
          author = input("Enter the author of the book: ")
          database.add_book(name, author)
          user_input = input(USER_CHOICE)
        elif user_input  == 'l':
          list_books()
          user_input = input(USER_CHOICE)
        elif user_input  == 'r':
          mark_book_as_read()
          user_input = input(USER_CHOICE)

        elif user_input  == 'd':
          delete_prompt_book()
          user_input = input(USER_CHOICE)




def list_books():
  books = database.get_all_books()
  for book in books:
    read = 'YES' if book['read'] else 'NO'
    print('The name of the book is : {0} by {1}'.format(book["name"],book["author"] ))


def mark_book_as_read():
  name = input("Please enter the name of the book: ")
  database.update_book(name)


def delete_prompt_book():
  name = input("Enter the book that your want do delete: ")
  database.delete_book(name)


menu()