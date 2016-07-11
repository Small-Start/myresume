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
		# parser_classes = (MultiPartParser, FormParser,)
		try :
			Data = request.data.copy()
			img = base64.b64decode(Data['image'].replace('data:image/jpeg;base64',''))
			if img:
				Data['image'] = ContentFile(img,request.user.username+'.jpg')
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