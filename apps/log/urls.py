from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
		url(r'^log',views.login),
		url(r'^process', views.process),
		url(r'^reg/(?P<id>\d+)$', views.reg),
		url(r'^$', views.index),
		]