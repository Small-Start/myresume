from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, Template
from django.contrib.auth import authenticate, login,logout
from forms import StudentForm
from models import Student
import json
from rest_framework import status
from rest_framework.response import Response
from serializers import StudentSerializer
from rest_framework.views import APIView
from django.http import Http404
from pprint import pprint

class index(View):

	def get(self, request):
		return HttpResponse("home page")

class Student1View(View):
	template = "temp.html"

	def get(self, request):
		return render(request, self.template, {})


class StudentView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
    	try :
            student =  Student.objects.get(person = request.user)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
    	except Student.DoesNotExist:
    		raise Http404
    def post(self, request, format=None):
        # parser_classes = (MultiPartParser, FormParser,)
        pprint(request.FILES)
        try :
            student =  Student.objects.get(person = request.user)
            serializer = StudentSerializer(student, data=request.data)
    	except Student.DoesNotExist:
            serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(person = request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
