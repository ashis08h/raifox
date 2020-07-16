from django.urls import path
from courseapp import views

urlpatterns=[
	path('', views.index, name='index'),
]
