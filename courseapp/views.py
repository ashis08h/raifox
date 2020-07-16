from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework import generics,permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# Create your views here.
def index(request):
	course_detail=Course.objects.all().order_by('-course_start_date')
	return render(request, 'courseapp/index.html',{'course_detail':course_detail})

class CourseList(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=Course.objects.all()
	serializer_class=CourseSerializer
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=Course.objects.all()
	serializer_class=CourseSerializer