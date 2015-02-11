from django.conf.urls import *
from url.views import index, redirect


urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^(?P<uuid>[^/]+)/', redirect),
	)
	