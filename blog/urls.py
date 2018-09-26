'''Import django path and blog views'''
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]

'''Assigning view called post_list'''