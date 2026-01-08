
import os
import sys

# 1. Imitar el parche de manage.py
try:
    import pymysql
    pymysql.install_as_MySQLdb()
    import MySQLdb
    setattr(MySQLdb, 'version_info', (2, 2, 1, 'final', 0))
    setattr(MySQLdb, '__version__', '2.2.1')
    print("Monkeypatch applied.")
except ImportError:
    print("Ex: PyMySQL not installed?")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autopartespro.settings")

import django
print("Setup Django...")
django.setup()
print("Django setup done.")

from django.db import connection
print("Attempting DB connection...")
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM productos_producto")
        res = cursor.fetchone()
        print(f"SUCCESS! Products found: {res[0]}")
except Exception as e:
    print(f"FAILURE: {e}")
