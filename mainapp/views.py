from django.shortcuts import render

from .models import Part_of_speech, Words

# контроллеры


def index(request):
    title = "Переводчик"
    content = {"title": title}
    return render(request, "mainapp/index.html", content)


def translator(request):
    title = "Переводчик"
    content = {"title": title}
    return render(request, "mainapp/translator.html", content)


def all_words(request, pk=None):
    title = "Все слова"
    words = Words.objects.all()
    cat_words = Part_of_speech.objects.all()
    content = {"title": title, "words": words, "cat_words": cat_words}

    if pk:
        print(f"User select word {pk}")
    # content = {"title": title}
    return render(request, "mainapp/all_words.html", content)


def training(request):
    title = "Тренировка"
    content = {"title": title}
    return render(request, "mainapp/training.html", content)
