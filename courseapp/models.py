from django.db import models

# Create your models here.
class Course(models.Model):
	course_title=models.CharField(max_length=100)
	category=models.CharField(max_length=100)
	description=models.TextField()
	language=models.CharField(max_length=100)
	image_url=models.URLField()
	course_start_date=models.DateTimeField(null=True)
	course_end_date=models.DateTimeField(null=True)
	# This is for return in sting
	def __str__(self):
		return self.course_title

