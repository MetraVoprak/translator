from django.shortcuts import render


def index(request):
    title = 'Переводчик'
    content = {"title": title}
    return render(request, "mainapp/index.html", content)


def all_words(request):
    title = 'Все слова'
    words = [
        {
            'eng':'hand', 
            'rus':'рука'
        },
        {
            'eng':'book', 
            'rus':'книга'
        },
        {
            'eng':'run', 
            'rus':'бежать'
        },
        {
            'eng':'city', 
            'rus':'город'
        }
    ]
    content = {"title": title, "words": words}
    # content = {"title": title}
    return render(request, "mainapp/all_words.html", content)


def training(request):
    title = 'Тренировка'
    content = {"title": title}
    return render(request, "mainapp/training.html", content) 