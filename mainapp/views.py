from django.shortcuts import render


def index(request):
    return render(request, "mainapp/index.html")


def all_words(request):
    return render(request, "mainapp/all_words.html")


def training(request):
    return render(request, "mainapp/training.html")
