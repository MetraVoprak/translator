from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.all_words, name='all_words'),
    # тут надо сделать доп страницу на каждое слово
    path("<int:pk>/", mainapp.all_words, name="categories")
]
