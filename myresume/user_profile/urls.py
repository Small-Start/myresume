from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index.as_view()),
	url(r'^student/$', views.StudentView.as_view()),
	url(r'^studentAPI/$', views.StudentAPI.as_view())
]