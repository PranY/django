from django.conf.urls import patterns, include, url
from django.contrib import admin
from url import urls as url_urls


urlpatterns = patterns('',
    url(r'^', include(url_urls)),
)
