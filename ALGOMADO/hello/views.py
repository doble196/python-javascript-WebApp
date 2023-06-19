from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")  # hello/index.html


def about(request):
    return render(request, "hello/about.html")  # hello/about.html


def result(request):
    return render(request, "hello/result.html")  # hello/result.html
