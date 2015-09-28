from django.conf.urls import patterns, url

from makemit.mailsignup import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)