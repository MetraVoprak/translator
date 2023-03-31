from django.shortcuts import render, get_object_or_404

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
    links_menu = Part_of_speech.objects.all()

    if pk is not None:
        if pk == 0:
            words = Words.objects.all()
            cat_words = {"name": "все"}
        else:
            cat_words = get_object_or_404(Part_of_speech, pk=pk)
            words = Words.objects.filter(category__pk=pk)

        content = {
            "title": title,
            "links_menu": links_menu,
            "words": words,
            "cat_words": cat_words
        }
        return render(request, "mainapp/all_words_list.html", content)

    words = Words.objects.all()
    cat_words = Part_of_speech.objects.all()
    content = {"title": title, "words": words,
               "links_menu": links_menu, "cat_words": cat_words}

    if pk:
        print(f"User select word {pk}")

    return render(request, "mainapp/all_words.html", content)


def training(request):
    title = "Тренировка"
    content = {"title": title}
    return render(request, "mainapp/training.html", content)
