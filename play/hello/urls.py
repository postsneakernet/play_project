from django.conf.urls import patterns, url

from hello import views

urlpatterns = patterns('',
    url(r'^$', views.hello, name='hello'),
    url(r'^html/$', views.hello_html, name='hello_html'),
)
