from rest_framework import serializers
from .models import Course

# serialization of course models data
class CourseSerializer(serializers.ModelSerializer):
	class Meta():
		model=Course
		fields='__all__'
