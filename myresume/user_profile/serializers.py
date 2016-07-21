from rest_framework import serializers
from .models import Student, Education,Project, Internship, Activity, Address
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email')


class EducationSerializer(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		many = kwargs.pop('many', True)
		super(EducationSerializer, self).__init__(many=many, *args, **kwargs)

	class Meta:
		model = Education
		extra_kwargs = {'id':{'required':False}, 'person':{'write_only':True,'required':False}}

	


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project

class InternshipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Internship

class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address

class StudentSerializer(serializers.ModelSerializer):
	person = UserSerializers(required=False)
	education = EducationSerializer(many=True, required=False, read_only =True)
	project = ProjectSerializer(many=True, required=False, read_only =True)
	internship = InternshipSerializer(many=True, required=False, read_only =True)
	activity = ActivitySerializer(many=True, required=False, read_only =True)
	address = AddressSerializer(many=True,required=False, read_only =True)
	class Meta:
		model = Student
		fields = ('person','name','contact','skills','dob','image','education','project','internship','activity','address')

