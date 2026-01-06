import os
import sys
import datetime
import subprocess
from decouple import config
from pathlib import Path

# Setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
BACKUP_DIR = BASE_DIR / 'backups'

def backup_database():
    print("--- Starting Database Backup ---")
    
    # Ensure backup directory exists
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Created backup directory: {BACKUP_DIR}")

    # Get credentials from env
    DB_NAME = config('DB_NAME', default='autopartespro')
    DB_USER = config('DB_USER', default='root')
    DB_PASSWORD = config('DB_PASSWORD', default='')
    DB_HOST = config('DB_HOST', default='localhost')
    DB_PORT = config('DB_PORT', default='3306')

    # Timestamp for filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"backup_{DB_NAME}_{timestamp}.sql"
    filepath = BACKUP_DIR / filename
    
    # Construct mysqldump command
    mysqldump_cmd = 'mysqldump'
    
    # Check for XAMPP specific path if global command not found
    xampp_path = r"C:\xampp\mysql\bin\mysqldump.exe"
    if os.path.exists(xampp_path):
        mysqldump_cmd = xampp_path
        print(f"Found XAMPP mysqldump at: {mysqldump_cmd}")
    
    cmd = [
        mysqldump_cmd,
        f'--host={DB_HOST}',
        f'--port={DB_PORT}',
        f'--user={DB_USER}',
        f'--password={DB_PASSWORD}',
        # ' --column-statistics=0', # Removed as it causes issues with some MariaDB versions in XAMPP
        '--single-transaction',  # Good for InnoDB
        '--quick',
        '--lock-tables=false',
        DB_NAME
    ]
    
    print(f"Dumping database '{DB_NAME}' to {filename}...")
    
    try:
        with open(filepath, 'w') as f:
            process = subprocess.Popen(cmd, stdout=f, stderr=subprocess.PIPE)
            _, stderr = process.communicate()
            
            if process.returncode != 0:
                print(f"Error dumping database: {stderr.decode('utf-8')}")
                return False
            
        print(f"Backup successful! File saved to: {filepath}")
        
        # Optional: Compress
        # Here we just leave as SQL for simplicity on Windows without forcing gzip install
        
        return True
    except FileNotFoundError:
        print("Error: 'mysqldump' command not found. Please ensure MySQL is installed and added to your PATH.")
        print("If you are using XAMPP, add 'C:\\xampp\\mysql\\bin' to your Environment Variables.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def rotate_backups(keep=5):
    """Keep only the last 'keep' files"""
    print(f"Rotating backups (keeping last {keep})...")
    files = sorted(BACKUP_DIR.glob('backup_*.sql'), key=os.path.getmtime, reverse=True)
    
    if len(files) > keep:
        for f in files[keep:]:
            try:
                os.remove(f)
                print(f"Deleted old backup: {f.name}")
            except OSError as e:
                print(f"Error removing {f.name}: {e}")
    else:
        print("No old backups to delete.")

if __name__ == "__main__":
    success = backup_database()
    if success:
        rotate_backups()
