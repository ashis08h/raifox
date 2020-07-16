from django.db import models

# Create your models here.
class Course(models.Model):
	course_title=models.CharField(max_length=100)
	category=models.CharField(max_length=100)
	description=models.TextField()
	language=models.CharField(max_length=100)
	image_url=models.URLField()
	course_start_date=models.DateTimeField()
	course_end_date=models.DateTimeField()
	def __str__(self):
		return self.course_title

