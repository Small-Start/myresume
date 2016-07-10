from rest_framework import serializers
from .models import Student, Education
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email')


class EducationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Education

class StudentSerializer(serializers.ModelSerializer):
	person = UserSerializers(required=False)
	education = EducationSerializer(many=True, required=False)
	class Meta:
		model = Student
		fields = ('person','name','contact','skills','dob','image','education')

