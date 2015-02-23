from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from play import views

urlpatterns = patterns('',
    url(r'^lessons/', include('lessons.urls')),
    url(r'^hello/', include('hello.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^about/', views.about, name="about"),
    url(r'^login/', views.login, name="login"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^user/', views.user, name="user"),
    url(r'^$', views.home, name="home"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.MEDIA_ROOT}))
