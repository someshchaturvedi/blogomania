from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.user_page,  name = 'user_page'),
	url(r'^saveblog/$' , views.save_blog, name = 'save_blog'),
]