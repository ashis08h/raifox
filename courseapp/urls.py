from django.urls import path
from courseapp import views

# This is for return index page which has all courses.
urlpatterns=[
	path('', views.index, name='index'),
]
