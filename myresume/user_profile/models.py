from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import RegexValidator

class Student(models.Model):
	"""
		Model for Student personal information
	"""
	phone_regx = RegexValidator(regex=r'^\d{10}$', message="Phone number must be ten digit")
	person = models.OneToOneField(User, primary_key=True)
	name = models.CharField(max_length = 50)
	contact = models.CharField(max_length = 10, validators=[phone_regx])
	skills = models.TextField(blank = True, null = True)
	image = models.ImageField(upload_to = 'images/', blank=True, null=True)
	dob = models.DateField()
	created = models.DateTimeField(auto_now_add = True)
	last_update = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.person.username

class Education(models.Model):
	"""
		Model for Storing Educational details
	"""
	person = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='education')
	course = models.CharField(max_length = 50)
	college = models.CharField(max_length = 50)
	board = models.CharField(max_length=50)
	# board field contain Board/University
	percentage = models.FloatField(default = 00.00) # percentage filed contain percentage as well as CGPA
	is_perchange = models.BooleanField(default = True) 
	# is_percentage will True if percentage field contain Percentage if it contain CGPA then is_percentage will False
	year = models.IntegerField(default = datetime.date.today().year)

	class Meta:
		unique_together = ('person', 'course', 'year')

	def __unicode__(self):
		return self.person.person.username + ' ' + self.course

class Project(models.Model):
	person = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='project')
	title = models.CharField(max_length = 50)
	technology = models.TextField()
	description = models.TextField()
	def __unicode__(self):
		return self.person.person.username+ ' ' + self.title


class Internship(models.Model):
	person = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='internship')
	company = models.CharField(max_length = 50)
	start_date = models.DateField()
	end_date  = models.DateField()
	role = models.CharField(max_length=50)
	def __unicode__(self):
		return self.person.person.username + ' ' + self.company


class Activity(models.Model):
	person = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='activity')
	event = models.CharField(max_length=50)
	place = models.CharField(max_length=50)
	role = models.CharField(max_length=50)

	def __unicode__(self):
		return self.person.person.username + ' ' + self.event

class Address(models.Model):
	person = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='address')
	line1 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	zip = models.IntegerField()
	def __unicode__(self):
		return self.person.person.username + ' ' + self.zip