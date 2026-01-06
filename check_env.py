import os
from decouple import config

print(f"OS Environ DEBUG: {os.environ.get('DEBUG')}")
try:
    print(f"Decouple DEBUG: {config('DEBUG')}")
except Exception as e:
    print(f"Decouple Error: {e}")
