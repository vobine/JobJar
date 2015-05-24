from django.conf.urls import patterns, url

from JobJarApplication import views

urlpatterns = patterns ('',
                        url (r'^$',
                             views.IndexView.as_view (),
                             name='index'))
