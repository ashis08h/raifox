from django.shortcuts import render
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# index function for all courses
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

# for crud api 
class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
