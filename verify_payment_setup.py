import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

def verify_payment_flow():
    print("1. Creating Test Order...")
    order_data = {
        "items": [
            {
                "id": 1,
                "cantidad": 1,
                "precio": 100
            }
        ],
        "cliente_nombre": "Test",
        "cliente_apellido": "User",
        "cliente_email": "test@user.com",
        "cliente_telefono": "123456789",
        "direccion_calle": "Test St",
        "direccion_numero": "123",
        "direccion_comuna": "TestComuna",
        "direccion_region": "TestRegion",
        "metodo_pago": "mercadopago"
    }
    
    products_resp = requests.get(f"{BASE_URL}/api/productos/")
    if products_resp.status_code == 200:
        results = products_resp.json().get('results', [])
        if results:
            order_data["items"][0]["id"] = results[0]["id"]
            order_data["items"][0]["precio"] = float(results[0]["precio_final"])

    try:
        response = requests.post(f"{BASE_URL}/api/ordenes/", json=order_data)
        if response.status_code != 201:
            print(f"Failed to create order: {response.text}")
            return
        
        order_id = response.json()['id']
        print(f"Order Created: {order_id}")
        
        print("2. Creating Preference...")
        pay_resp = requests.post(f"{BASE_URL}/api/ordenes/{order_id}/pagar_mercadopago/")
        print(f"Status: {pay_resp.status_code}")
        print(f"Response: {pay_resp.text}")
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    verify_payment_flow()
