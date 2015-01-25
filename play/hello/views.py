from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, world!")

def hello_html(request):
    context = {'hello': "Hello, world!"}
    return render(request, 'hello/hello.html', context)
