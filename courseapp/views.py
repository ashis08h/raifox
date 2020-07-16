from django.shortcuts import render
from .models import Course
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import CourseSerializer
from rest_framework import generics,permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# Create your views here.
def index(request):
	course_detail=Course.objects.all().order_by('-course_start_date')
	paginator = Paginator(course_detail, 8)
	page = request.GET.get('page')
	try:
		course_details = paginator.page(page)
	except EmptyPage:
		course_details = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		course_details = paginator.page(1)
	return render(request, 'courseapp/index.html',{'course_details': course_details})

class CourseList(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=Course.objects.all()
	serializer_class=CourseSerializer
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=Course.objects.all()
	serializer_class=CourseSerializer