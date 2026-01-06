import os
from decouple import config
import sys

def check_security():
    print("--- Security Configuration Check ---")
    
    # Check env vars
    ssl_redirect = config('SECURE_SSL_REDIRECT', default=False, cast=bool)
    session_secure = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
    csrf_secure = config('CSRF_COOKIE_SECURE', default=False, cast=bool)
    
    print(f"SECURE_SSL_REDIRECT: {'[OK] Enabled' if ssl_redirect else '[WARNING] Disabled (Enable for Production)'}")
    print(f"SESSION_COOKIE_SECURE: {'[OK] Enabled' if session_secure else '[WARNING] Disabled (Enable for Production)'}")
    print(f"CSRF_COOKIE_SECURE: {'[OK] Enabled' if csrf_secure else '[WARNING] Disabled (Enable for Production)'}")
    
    # Check settings.py content (basic check)
    try:
        with open('autopartespro/settings.py', 'r', encoding='utf-8') as f:
            content = f.read()
            if "SECURE_BROWSER_XSS_FILTER = True" in content:
                print("SECURE_BROWSER_XSS_FILTER: [OK] Found in settings")
            else:
                print("SECURE_BROWSER_XSS_FILTER: [FAIL] Not found in settings")
                
            if "X_FRAME_OPTIONS = 'DENY'" in content:
                print("X_FRAME_OPTIONS: [OK] Set to DENY")
            else:
                print("X_FRAME_OPTIONS: [FAIL] Not set to DENY")
    except Exception as e:
        print(f"Error reading settings.py: {e}")

    # Check index.html for anti-copy
    try:
        with open('web/templates/index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            if "document.addEventListener('contextmenu'" in content:
                print("Frontend Anti-Right-Click: [OK] Found")
            else:
                print("Frontend Anti-Right-Click: [FAIL] Not found")
                
            if "Pago Seguro SSL" in content:
                print("Trust Badge: [OK] Found")
            else:
                print("Trust Badge: [FAIL] Not found")
    except Exception as e:
        print(f"Error reading index.html: {e}")

if __name__ == "__main__":
    # Mock decouple if not installed or env issue, since we just want to verify logic locally usually
    # But here we assume context.
    try:
        from decouple import config
    except ImportError:
        print("python-decouple not found. Please install it.")
        sys.exit(1)
        
    check_security()
