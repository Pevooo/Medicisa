# Medicisa
Medicisa is a comprehensive mobile application designed to empower individuals to take control of their health and well-being. Whether you're managing a chronic condition, looking to seek expert medical advice, Medicisa provides all the tools and resources you need in one convenient platform.
This project was made using Flutter, Firebase, Flask

## 1. API

### 1.1 Description
The api is built using Flask with Python. Its job is to interact with **Firebase Realtime Database**.
The latest version of the api can be accessed through this link: *Pevooo.pythonanywhere.com*

### 1.2 How To Use
You can use the api by sending an http request including json in the body of the request, then the api send a suitable response to that request. A secret key has to be included in every request for authorization.
The api will send status if an ooperation was successful or not.
###### Success
```
{
  "status": 1
}
```
###### Failure
```
{
  "status": 0
}
```


##### 1.2.1 Registration
You can register a new user in the database by sendinng a **POST** request to: *Pevooo.pythonanywhere.com/add/{id}* where "{id}" represents the id of the new user.
###### Example
```
{
  "key": "SECRET KEY HERE",
  "name": "NAME HERE",
  "phonenumber": "PHONE NUMBER HERE",
  "password": "PASSWORD HERE",
  "type": "Doctor / Patient"
}
```

##### 1.2.2 Login
You can access an account details by sendinng a **POST** request to: *Pevooo.pythonanywhere.com/get/{id}* where "{id}" represents the id of the new user.
###### Example
```
{
  "key": "SECRET KEY HERE",
  "password": "PASSWORD HERE"
}
```

##### 1.2.3 Uploading Reports
You can upload a report as an image by sending a **POST** request to *Pevooo.pythonanywhere.com/upload_report/{id}* where "{id}" represents the id of the new user. The photo has to be represented as a string.
###### Example 
```
{
  "key": "SECRET KEY HERE",
  "filename": "FILENAME HERE",
  "filedata": "FILE DATA HERE"
}
```

## 2. Flutter Application

### 2.1 Description
The application was made using Flutter. All of the flutter code is in the *app* folder including all of the dependencies needed to use the application

