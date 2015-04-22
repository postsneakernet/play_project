from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from lessons.models import Lesson

def home(request):
    lessons = Lesson.objects.published().order_by('-modified')[:3]

    return render(request, 'home.html', {'lessons': lessons})

def about(request):
    about = "about"

    return render(request, 'about.html', {'about': about})

def error404(request):
    return render(request, '404.html')
