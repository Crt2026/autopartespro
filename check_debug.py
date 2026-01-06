from decouple import config
try:
    print(f"DEBUG raw: {config('DEBUG')}")
    print(f"DEBUG bool: {config('DEBUG', cast=bool)}")
except Exception as e:
    print(f"Error: {e}")
