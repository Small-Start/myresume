from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
	Confirm_password = serializers.CharField(write_only = True)
	email  = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(),
		message="You are already registered with same Email Address")])
	class Meta:
		model = User
		fields = ('username','password','email','Confirm_password')
		extra_kwargs = {'password':{'write_only':True}}
		
	def validate(Self, data):
		"""
		Check that the password and confirm_password should match.
		"""
		if data.get('password') != data.get('Confirm_password'):
			raise serializers.ValidationError("password does not confirm")
		data.pop('Confirm_password',None)
		return data

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=30)

	def Authenticate(self, data):
		user = authenticate(username=data.get('username'),password=data.get('password'))
		if user is not None:
			if user.is_active:
				return user
			raise serializers.ValidationError("Your account is deactivated")
		raise serializers.ValidationError('Either username or password is wrong')