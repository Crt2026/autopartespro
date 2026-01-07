
import pymysql
import sys

print("Testing connection to 127.0.0.1:3306 using PyMySQL...")
try:
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='autopartespro',
        cursorclass=pymysql.cursors.DictCursor,
        read_timeout=5
    )
    print("SUCCESS: Connected with PyMySQL!")
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) as count FROM productos_producto")
        result = cursor.fetchone()
        print(f"Products: {result['count']}")
    
    connection.close()

except Exception as e:
    print(f"FAILED: {e}")
