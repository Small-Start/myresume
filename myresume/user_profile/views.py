from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, Template
from django.contrib.auth import authenticate, login,logout
# Create your views here.


class index(View):

	def get(self, request):
		return HttpResponse("home page")