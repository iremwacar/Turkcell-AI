import requests

baseUrl = "http://localhost:3000/products"

def getProducts():
    response =requests.get(baseUrl)
    print(response.json())
    
products = getProducts()

for product in products:
    product.quantityPerUnit

