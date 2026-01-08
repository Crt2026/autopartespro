import django
from django.db.backends.mysql.base import DatabaseWrapper

def monkey_patch_db_check():
    # Bypass the database version check
    def check_database_version_supported(self):
        print(f"Skipping database version check for {self.vendor}...")
        return

    DatabaseWrapper.check_database_version_supported = check_database_version_supported
