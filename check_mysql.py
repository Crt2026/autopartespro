import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
print(f"Version info: {getattr(MySQLdb, 'version_info', 'Not Found')}")
if hasattr(MySQLdb, 'version_info'):
    print(f"Version info type: {type(MySQLdb.version_info)}")
    print(f"Version info < (1,4,3): {MySQLdb.version_info < (1, 4, 3)}")

# Apply patch
if not hasattr(MySQLdb, 'version_info') or MySQLdb.version_info < (1, 4, 3):
    MySQLdb.version_info = (1, 4, 6, 'final', 0)
    MySQLdb.__version__ = '1.4.6'

print(f"Patched Version info: {MySQLdb.version_info}")
print(f"Patched Version info < (1,4,3): {MySQLdb.version_info < (1, 4, 3)}")
