from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from quizzes.models import Question, Answer
from lessons.models import Lesson

class QuizIndex(generic.ListView):
    template_name = 'quizzes.html'
    context_object_name = 'quizzes'

    def get_queryset(self):
        return Lesson.objects.published


def quiz_detail(request, lesson_slug):
    questions = Question.objects.published().filter(lesson__slug=lesson_slug)
    answers = Answer.objects.all().filter(question__lesson__slug=lesson_slug)

    return render(request, 'quiz_detail.html', {'questions': questions,
            'answers': answers,
            })

def quiz_results(request):
    questions = ""
    answers = ""
    #questions = Question.objects.published().filter(lesson__slug=lesson_slug)
    #answers = Answer.objects.all().filter(question__lesson__slug=lesson_slug)

    return render(request, 'quiz_results.html', {'questions': questions,
            'answers': answers,
            })
