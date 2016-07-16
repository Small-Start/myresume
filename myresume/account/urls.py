from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$',views.Login.as_view()),
	url(r'^register/$',views.Register.as_view()),
	url(r'^logout/$',views.logoff.as_view()),
]