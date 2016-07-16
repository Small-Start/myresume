from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
import json
from pprint import pprint
from rest_framework import status
from rest_framework.response import Response
from serializers import UserSerializer, LoginSerializer
from rest_framework.views import APIView
from django.http import Http404

class Register(APIView):
	template = "account.html"
	def get(self,request):
		return render(request, self.template,{})

	def post(self, request, format=None):
		serializer = UserSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
	def post(self, request, format = None):
		serializer = LoginSerializer(data = request.data)
		if serializer.is_valid():
			user = serializer.Authenticate(request.data)
			login(request,user)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class logoff(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect('/')