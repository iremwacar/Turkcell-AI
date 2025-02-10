import requests

baseUrl = "http://localhost:3000/products"

def getProducts():
    response =requests.get(baseUrl)
    print(response.json())
    

#create
def createProduct(product):
    response =requests.post(baseUrl,json=product)
    return response.json()

createProduct(
    {
        "supplierId": 2,
        "categoryId": 3,
        "quantityPerUnit": "36 boxes",
        "unitPrice": 321.35,
        "unitsInStock": 0,
        "unitsOnOrder": 0,
        "reorderLevel": 0,
        "discontinued": True,
        "name": "Mikrofon 2"
    }
)



#update
def updateProduct(id, product):
    response = requests.put(baseUrl + "/" + str(id), json=product)  # PUT yöntemi kullanıyoruz
    print("Status Code:", response.status_code)  # Yanıt kodunu yazdır
    print("Response Text:", response.text)  # Yanıtı kontrol et
    try:
        return response.json()  # JSON'a dönüştürmeyi deneyin
    except ValueError:
        print("JSON Decode Error: Response is not in JSON format.")
        return None  # Eğer JSON formatında değilse None döndürebiliriz

updateProduct("dab1", {
    "supplierId": 2,
    "categoryId": 3,
    "quantityPerUnit": "36 boxes",
    "unitPrice": 321.35,
    "unitsInStock": 0,
    "unitsOnOrder": 0,
    "reorderLevel": 0,
    "discontinued": True,
    "name": "Mikrofon 3"
})


#delete
def deleteProduct(id):
    response = requests.delete(baseUrl + "/" + str(id)) 
    
deleteProduct("dab1")

def postCategory(postCategory):
    if postCategory.get("name") != category.get("name"):
        response = requests.post(baseUrl, json=postCategory)
        return response.json()
    else:
        print("name kısmı aynı olamaz")
    

postCategory({
    "description": "Deneme5",
    "name": "Deneme5",
})

def putCategory(id,putCategory):
    if putCategory.get("name") == category.get("name"):
        response = requests.put(baseUrl+"/"+str(id),json=putCategory)
        return response.json()
    else:
        print("name kısmı aynı olmak zorunda")
    

putCategory("4e1b",{
    "description": "Deneme6",
    "name": "Deneme6",
})