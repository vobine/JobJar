from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url ('^JobJar/',
                            include ('JobJarApplication.urls',
                                     namespace='jobjar')),
                       url(r'^admin/', 
                           include(admin.site.urls)),
)
