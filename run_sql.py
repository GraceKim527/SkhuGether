from django.db import connection
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'getherprj.settings')

def my_custom_sql(sql_file_name):
    with connection.cursor() as cursor:
        sql_file = open(sql_file_name, encoding='UTF-8')
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)

my_custom_sql("model.db.sql")