from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from lessons.models import Lesson, File

class LessonIndex(generic.ListView):
    template_name = 'lessons.html'
    context_object_name = 'lessons'

    def get_queryset(self):
        return Lesson.objects.published

def lesson_detail(request, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    files = File.objects.filter(lesson__slug=lesson_slug)

    return render(request, 'lesson_detail.html', {'lesson': lesson,
            'files': files})
