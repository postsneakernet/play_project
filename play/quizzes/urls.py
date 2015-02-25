from django.conf.urls import patterns, url
from quizzes import views


urlpatterns = patterns(
    '',
    url(r'^$', views.QuizIndex.as_view(), name="quiz_index"),
    url(r'^results/$', views.quiz_results, name="quiz_results"),
    url(r'^(?P<lesson_slug>\S+)/$', views.quiz_detail, name="quiz_detail"),
)
