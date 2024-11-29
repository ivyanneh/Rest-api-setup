import requests
import json

# Base URL for the API
BASE_URL = 'http://127.0.0.1:5000/products'

def add_product(name, description, price):
    product = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(BASE_URL, json=product)
    if response.status_code == 201:
        print('Product added successfully:', response.json())
    else:
        print('Failed to add product:', response.json())

def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        products = response.json()
        print('Products:')
        print(json.dumps(products, indent=4))
    else:
        print('Failed to retrieve products:', response.json())

if __name__ == '__main__':
    # Example usage
    add_product('Laptop', 'A high performance laptop', 1200.99)
    add_product('Smartphone', 'A latest generation smartphone', 699.99)
    get_products()
