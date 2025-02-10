import requests

baseUrl="http://localhost:3000/category"

def getCategories():
    response = requests.get(baseUrl)
    return response.json() 

def getCategoryById(id):
    response = requests.get(baseUrl+'/'+str(id))
    return response.json()

categories = getCategories()

for category in categories:
    print(category.get("name"))


def createCategory(category):
    response =requests.post(baseUrl,json=category)
    return response.json()
"""
createCategory(
    {
        "name": "ortaokul",
        "description": "Ortaokula giden öğrencileri içerir."
    }
)
"""

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

def deleteCategory(id):
    response = requests.delete(baseUrl + "/" + str(id)) 
    




def patchCategory(id,patchCategory):
        response = requests.patch(baseUrl+"/"+str(id), json=patchCategory)
        return response.json()
 
patchCategory("0048",
              {"description": "Deneme",
               "name":"Deneme5"})

def putCategory(id,patchCategory):
        response = requests.put(baseUrl+"/"+str(id), json=patchCategory)
        return response.json()






#COURSE
baseUrlCourse="http://localhost:3000/course"

def getCourse():
    response = requests.get(baseUrlCourse)
    return response.json() 

def getCoursesById(id):
    response = requests.get(baseUrlCourse+'/'+str(id))
    return response.json()

courses = getCourse()

for course in courses:
    print(course.get("title"))


def createCourse(course):
    response =requests.post(baseUrlCourse,json=course)
    return response.json()
"""
createCourse(
    {
        "title": "YKS",
        "description": "YKS müfredati içerir.",
        "price":"5000",
        "category_id":"0048",
        "created_at":"10.02.2025"
    }
)
"""

def postCourse(postCourse):
    if postCourse.get("title") != course.get("title"):
        response = requests.post(baseUrlCourse, json=postCourse)
        return response.json()
    else:
        print("title kısmı aynı olamaz")
    

postCourse({
        "title": "YKS",
        "description": "YKS müfredati içerir.",
        "price":"5200",
        "category_id":"0048",
        "created_at":"10.02.2025"
})


def deleteCourse(id):
    response = requests.delete(baseUrlCourse + "/" + str(id)) 
    
deleteCourse("8337")
    

def patchCourse(id,patchCourse):
        response = requests.patch(baseUrlCourse+"/"+str(id), json=patchCourse)
        return response.json()
 
patchCourse("94dc",
              {"price":"5200"})

def putCourse(id,patchCourse):
        response = requests.put(baseUrlCourse+"/"+str(id), json=patchCourse)
        return response.json()






#LESSON

baseUrlLesson="http://localhost:3000/lesson"

def getLesson():
    response = requests.get(baseUrlLesson)
    return response.json() 

def getLessonsById(id):
    response = requests.get(baseUrlLesson+'/'+str(id))
    return response.json()

lessons = getLesson()

for lesson in lessons:
    print(lesson.get("title"))


def createLesson(Lesson):
    response =requests.post(baseUrlLesson,json=Lesson)
    return response.json()
"""
createLesson(
    {
        "title": "Matematik",
        "content": "Matematik ders müfredati içerir.",
        "video_url":"http...",
        "course_id":"94dc"
    }
)
"""

def postLesson(postLesson):
    if postLesson.get("title") != lesson.get("title"):
        response = requests.post(baseUrlLesson, json=postLesson)
        return response.json()
    else:
        print("title kısmı aynı olamaz")
    
"""
postLesson({
       "title": "Türkçe2",
        "content": "Türkçe ders müfredati içerir.",
        "video_url": "http...",
        "course_id": "94dc"
})
"""


def deleteLesson(id):
    response = requests.delete(baseUrlLesson + "/" + str(id)) 
    
deleteLesson("2e15")


def patchLesson(id,patchLesson):
        response = requests.patch(baseUrlLesson+"/"+str(id), json=patchLesson)
        return response.json()
 
patchLesson("9c36",
              {"video_url": "http2...",
               "content": "Türkçe dersinin müfredati içerir.",})

def putLesson(id,putLesson):
    if putLesson.get("title")==lesson.get("title"):
        response = requests.put(baseUrlLesson+"/"+str(id), json=putLesson)
        return response.json()
    else:
        print("title kısmı aynı olmak zorunda")
    
putLesson("7c5d",
          {"title": "Türkçe2",
            "content": "Türkçe ders müfredati içerir.",
            "video_url": "http...",
            "course_id": "94dc"})






#Student

baseUrlStudent="http://localhost:3000/student"

def getStudent():
    response = requests.get(baseUrlStudent)
    return response.json() 

def getStudentsById(id):
    response = requests.get(baseUrlStudent+'/'+str(id))
    return response.json()

students = getStudent()

for student in students:
    print(student.get("name"))


def createStudent(student):
    response =requests.post(baseUrlStudent,json=student)
    return response.json()
"""
createStudent(
    {
        "name": "irem",
        "email": "irem@gmail.com",
        "password":"1234",
        "enrollment":{
            "id":"1",
            "status":"Tamamlandı",
            "endrolled_at":"10.02.2025"
        }
    }
)
"""


def postStudent(postStudent):
    if postStudent.get("name") != student.get("name"):
        response = requests.post(baseUrlStudent, json=postStudent)
        return response.json()
    else:
        print("name kısmı aynı olamaz")
    

postStudent({
       "title": "Tülin",
        "email": "tülin@gmail.com",
        "password": "1234",
        "enrollment": {
            "id": "1",
            "status": "Tamamlandı",
            "endrolled_at": "11.01.2025"
    }
})



def deleteStudent(id):
    response = requests.delete(baseUrlStudent + "/" + str(id)) 
    
deleteStudent("d0d2")



def patchStudent(id,patchStudent):
        response = requests.patch(baseUrlStudent+"/"+str(id), json=patchStudent)
        return response.json()
 
patchStudent("39c4",
              {"password": "123..."})



def putStudent(id,putStudent):
    if putStudent.get("title")==student.get("title"):
        response = requests.put(baseUrlStudent+"/"+str(id), json=putStudent)
        return response.json()
    else:
        print("title kısmı aynı olmak zorunda")
    
putStudent("7c5d",
          {
        "id": "477d",
        "name": "irem",
        "email": "irem@gmail.com",
        "password": "123456",
        "enrollment": {
            "id": "1",
            "status": "Tamamlandı",
            "endrolled_at": "10.02.2025"
        }
  })











#Payment

baseUrlPayment="http://localhost:3000/payment"

def getPayment():
    response = requests.get(baseUrlPayment)
    return response.json() 

def getPaymentsById(id):
    response = requests.get(baseUrlPayment+'/'+str(id))
    return response.json()

Payments = getPayment()

for Payment in Payments:
    print(Payment.get("status"))


def createPayment(Payment):
    response =requests.post(baseUrlPayment,json=Payment)
    return response.json()
"""
createPayment(
    {
        "student_id":"477d",
        "course_id":"94dc",
        "amount":"5200",
        "status":"başarılı",
        "paid_at":"10.02.2025"
    }
)

"""
def postPayment(postPayment):
    if postPayment.get("student_id") != Payment.get("student_id"):
        response = requests.post(baseUrlPayment, json=postPayment)
        return response.json()
    else:
        print("student_id kısmı aynı olamaz")
    

postPayment({
    "student_id": "477d",
    "course_id": "94dc",
    "amount": "5200",
    "status": "başarılı",
    "paid_at": "11.02.2025"
})



def deletePayment(id):
    response = requests.delete(baseUrlPayment + "/" + str(id)) 
    
deletePayment("be4d")


def patchPayment(id,patchPayment):
        response = requests.patch(baseUrlPayment+"/"+str(id), json=patchPayment)
        return response.json()
 
patchPayment("37d7",
              {"student_id": "477d",
                "course_id": "94dc",
                "amount": "5000",
            
  })

def putPayment(id,putPayment):
    if putPayment.get("student_id")==Payment.get("student_id"):
        response = requests.put(baseUrlPayment+"/"+str(id), json=putPayment)
        return response.json()
    else:
        print("student_id kısmı aynı olmak zorunda")
    
putPayment("37d7",
          {
            "student_id": "477d",
            "course_id": "94dc",
            "amount": "5100",
            "status": "başarılı",
            "paid_at": "10.02.2025"
  })


  
        