
import mysql.connector
import sys

print("Testing connection to 127.0.0.1:3306...")
try:
    cnx = mysql.connector.connect(
        user='root', 
        password='',
        host='127.0.0.1',
        database='autopartespro',
        connection_timeout=5
    )
    print("SUCCESS: Connected to database!")
    
    cursor = cnx.cursor()
    cursor.execute("SELECT count(*) FROM productos_producto")
    count = cursor.fetchone()[0]
    print(f"Products in DB: {count}")
    cnx.close()
    
except mysql.connector.Error as err:
    print(f"FAILED: {err}")
except Exception as e:
    print(f"ERROR: {e}")
