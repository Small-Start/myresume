from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index.as_view()),
	url(r'^student/$', views.StudentView.as_view()),
	url(r'^studentAPI/$', views.StudentAPI.as_view()),
	url(r'^student/(?P<pk>[\w.@+-]{1,30})/$', views.StudentDetail.as_view()),
	url(r'^education/$', views.EducationView.as_view())
]