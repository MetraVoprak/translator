from django.shortcuts import render
from .models import Words, Part_of_speech


def index(request):
    title = 'Переводчик'
    content = {"title": title}
    return render(request, "mainapp/index.html", content)


def all_words(request):
    title = 'Все слова'
    words = Words.objects.all()
    content = {"title": title, "words": words}
    # content = {"title": title}
    return render(request, "mainapp/all_words.html", content)


def training(request):
    title = 'Тренировка'
    content = {"title": title}
    return render(request, "mainapp/training.html", content)
