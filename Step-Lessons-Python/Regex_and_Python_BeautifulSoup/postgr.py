'''Напишите программу с использованием pymssql или pymysql или psycopg2 или cx_Oracle, которая
выведет на экран данные из таблицы OPER'''

import psycopg2


try:
  connection = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 88888888,
  )
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM OPER")
  rows = cursor.fetchall()
  print(rows)

except (Exception, psycopg2.Error) as error:
  print('Ошибка при подлкючении к бд: ', error)



