from django.shortcuts import render
from .models import Course
# Create your views here.
def index(request):
	course_detail=Course.objects.all().order_by('-course_start_date')
	return render(request, 'courseapp/index.html',{'course_detail':course_detail})