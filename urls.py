from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns ('',
                        url (r'^JobJar/',
                             include ('JobJarApplication.urls')),
                        url (r'^admin/',
                             include (admin.site.urls)),
                        )
