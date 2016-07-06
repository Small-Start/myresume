from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email')

class StudentSerializer(serializers.ModelSerializer):
	person = UserSerializers(required=False)

	class Meta:
		model = Student
