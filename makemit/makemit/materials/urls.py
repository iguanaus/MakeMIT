from django.conf.urls import patterns, url

from makemit.materials import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^tutorials/', views.tutorials, name='tutorials')
)
