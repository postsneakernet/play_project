from django.conf.urls import patterns, url
from lessons import views

urlpatterns = patterns(
    '',
    url(r'^$', views.LessonIndex.as_view(), name="lesson_index"),
    url(r'^(?P<lesson_slug>\S+)$', views.lesson_detail, name="lesson_detail"),
)
