**Version 1.0.0**

A readme for CRUD Api of all Courses available on our website.

## Contributers 

-Ashish Kumar <ashis08h@gmail.com> 

---

## Technologies

	Python 3.8.2
	Django 3.0.5
	
---
## Library

	djano restframework
	django-oauth-toolkit
  
---
## Launch

 GitHub - https://github.com/ashis08h/raifox
 
## All links

for all course page - http://127.0.0.1:8000/allcourse/
for api - http://127.0.0.1:8000/course/ (you have to autherize you by access token)
for register appication first you have to login as admin on http://127.0.0.1:8000.admin then get client id on -http://127.0.0.1:8000/o/applications/
you can create new also there.
Superusername - ashish
Password - Ashish123@

 
## Description of Project

I made the crud api with django restframework in which i used Model Serializer to do serialization, and in views i used ModelViewSet to operate CRUD API.
After creation of the API i authorized that api by Django OAuth Toolkit ie oauth2 autherisation.
For testing purpose about autherization of api i used git bash tool.

For register appication - http://127.0.0.1:8000/o/applications/
from here we get the client id and client secret.
To create access token i used git bash and execute - curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
and entered my super username,password,client id, client secret.
After getting access token and become an authorized person we can access our api
for geting api we use - curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/course/
for posting some new data we use - curl -H "Authorization: Bearer <your_access_token>" -X POST -d"course_title=abc&category=abc......." http://localhost:8000/course/
In all courses page i add django paginator module to make pagination and i keep 8 objects in one page. and for mobile response i used bootstrap 4 classes. 

##Reference 
https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html
https://www.django-rest-framework.org/topics/documenting-your-api/

## License & copyright

Raifox.

