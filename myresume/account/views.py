from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, Template
from .forms import login_form,register_form
from django.contrib.auth import authenticate, login,logout
import json
from pprint import pprint


class register(View):
	template = "account.html"
	def get(self,request):
		return render(request, self.template,{})
	
	def post(self,request):
		error=""
		response = {'status' : 'fail'}
		if 'register' in request.POST:
			form = register_form(data = request.POST)
			if form.is_valid():
				form.cleaned_data.pop('Confirm_password')
				User.objects.create_user(**form.cleaned_data)
				user = authenticate(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
				login(request,user)
				#form.mail_send()
				response['status'] = "sucess"
				return HttpResponse(json.dumps(response),
					content_type = 'application/json')
			
			errors = form.errors
			for key in errors.keys():
				response[key] = errors[key]
			return HttpResponse(json.dumps(response),
				content_type = 'application/json')
		else :
			form = login_form(data = request.POST)
			if form.is_valid():
				username =  form.cleaned_data['username']
				password =  form.cleaned_data['password']
				user = authenticate(username = username,password = password)
				if user is not None :
					if user.is_active:
						login(request,user)
						response['status'] = "sucess"
						return HttpResponse(json.dumps(response),
							content_type = 'application/json')
					else :
						error = "User account is deactivated"
						response['error'] = error
				else :
					error = "username and password does not match"
					response['error']  = error
			errors = form.errors
			for key in errors.keys():
				response[key] = errors[key]
			return HttpResponse(json.dumps(response),
				content_type='application/json')

class logoff(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect('/')