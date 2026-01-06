import mercadopago
from decouple import config
import json

# Hardcoding credentials for the test script based on what we know
ACCESS_TOKEN = "APP_USR-5121172436691029-122522-f9be1f8e71b3035871cba14be1ab4521-2914738060"

def test_preference():
    print("Initializing SDK...")
    sdk = mercadopago.SDK(ACCESS_TOKEN)
    
    # Test 1: Localhost (This often fails with auto_return on some versions/accounts)
    print("\n--- TEST 1: HOST LOCALHOST ---")
    preference_data_local = {
        "items": [
            {
                "title": "Producto de prueba",
                "quantity": 1,
                "unit_price": 100,
                "currency_id": "CLP"
            }
        ],
        "back_urls": {
            "success": "http://localhost:8000/success",
            "failure": "http://localhost:8000/failure",
            "pending": "http://localhost:8000/pending"
        },
        "auto_return": "approved",
        "binary_mode": True
    }
    
    try:
        response = sdk.preference().create(preference_data_local)
        if response["status"] == 201:
            print("SUCCESS! Init Point:", response["response"]["init_point"])
        else:
            print("FAILED:", response["status"])
            print("Error:", response.get("response"))
    except Exception as e:
        print("EXCEPTION:", str(e))

    # Test 2: Public URL (Google)
    print("\n--- TEST 2: PUBLIC URL ---")
    preference_data_public = {
        "items": [
             {
                "title": "Producto de prueba",
                "quantity": 1,
                "unit_price": 100,
                "currency_id": "CLP"
            }
        ],
        "back_urls": {
            "success": "https://www.google.com/success",
            "failure": "https://www.google.com/failure",
            "pending": "https://www.google.com/pending"
        },
        "auto_return": "approved",
    }
    
    try:
        response = sdk.preference().create(preference_data_public)
        if response["status"] == 201:
            print("SUCCESS! Init Point:", response["response"]["init_point"])
        else:
            print("FAILED:", response["status"])
            print("Error:", response.get("response"))
    except Exception as e:
        print("EXCEPTION:", str(e))

if __name__ == "__main__":
    test_preference()
