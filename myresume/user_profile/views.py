from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from models import Student, Education
from rest_framework import status
from rest_framework.response import Response
from serializers import StudentSerializer, EducationSerializer
from rest_framework.views import APIView
from django.http import Http404
from pprint import pprint
import base64
from django.core.files.base import ContentFile
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import os
class index(View):

	def get(self, request):
		return HttpResponse("home page")

class StudentView(View):
	template = "temp.html"

	def get(self, request):
		return render(request, self.template, {})
	def post(self, request):
		return HttpResponse('Direct post request is not available, send data through API')

class StudentAPI(APIView):
	"""
	List all snippets, or create a new snippet.
	"""
	permission_classes = (IsAuthenticated,)
	def get(self, request, format=None):
		try :
			student =  Student.objects.get(person = request.user)
			serializer = StudentSerializer(student)
			return Response(serializer.data)
		except Student.DoesNotExist:
			raise Http404
	def post(self, request, format=None):
		try :
			os.remove(settings.MEDIA_ROOT + '/' + request.user.username) # removing old image
		except :
			pass
		try :
			Data = request.data.copy()
			ext, imgstr = Data['image'].split(';base64,')
			extention = ext.split('/')[-1]
			Data['image'] = ContentFile(base64.b64decode(imgstr),name=request.user.username) # saving image
		except:
			pass
		try :
			student =  Student.objects.get(person = request.user)
			serializer = StudentSerializer(student, data=Data)
		except Student.DoesNotExist:
			serializer = StudentSerializer(data=Data)
		if serializer.is_valid():
			serializer.save(person = request.user)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
	def get(self, request, pk):
		try :
			user = User.objects.get(username=pk)
			student = Student.objects.get(pk=user)
			serializer = StudentSerializer(student)
			return Response(serializer.data)
		except:
			return HttpResponse(status=404)

class EducationView(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self,request):
		student =  Student.objects.get(person = request.user)
		education = Education.objects.filter(person = student)
		serializer = EducationSerializer(education, many = True)
		return Response(serializer.data)

	def post(self, request):
		student =  Student.objects.get(person = request.user).person
		print request.user
		Data = request.data.copy()
		Data['person'] = student
		print Data
		serializer = EducationSerializer(data=Data, many=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
