#Payment

baseUrlPayment="http://localhost:3000/Payment"

def getPayment():
    response = requests.get(baseUrlPayment)
    return response.json() 

def getPaymentsById(id):
    response = requests.get(baseUrlPayment+'/'+str(id))
    return response.json()

Payments = getPayment()

for Payment in Payments:
    print(Payment.get("title"))


def createPayment(Payment):
    response =requests.post(baseUrlPayment,json=Payment)
    return response.json()
"""
createPayment(
    {
        "title": "Matematik",
        "content": "Matematik ders müfredati içerir.",
        "video_url":"http...",
        "course_id":"94dc"
    }
)
"""

def postPayment(postPayment):
    if postPayment.get("title") != Payment.get("title"):
        response = requests.post(baseUrlPayment, json=postPayment)
        return response.json()
    else:
        print("title kısmı aynı olamaz")
    
"""
postPayment({
       "title": "Türkçe2",
        "content": "Türkçe ders müfredati içerir.",
        "video_url": "http...",
        "course_id": "94dc"
})
"""


def deletePayment(id):
    response = requests.delete(baseUrlPayment + "/" + str(id)) 
    
deletePayment("2e15")


def patchPayment(id,patchPayment):
        response = requests.patch(baseUrlPayment+"/"+str(id), json=patchPayment)
        return response.json()
 
patchPayment("9c36",
              {"video_url": "http2...",
               "content": "Türkçe dersinin müfredati içerir.",})

def putPayment(id,putPayment):
    if putPayment.get("title")==Payment.get("title"):
        response = requests.put(baseUrlPayment+"/"+str(id), json=putPayment)
        return response.json()
    else:
        print("title kısmı aynı olmak zorunda")
    
putPayment("7c5d",
          {"title": "Türkçe2",
            "content": "Türkçe ders müfredati içerir.",
            "video_url": "http...",
            "course_id": "94dc"})