from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.all_words, name="all_words"),
    path("add_new_word/", mainapp.addword, name="addword"),
    path("upd_word/", mainapp.updword, name="updword"),
    path("category/<int:pk>/", mainapp.all_words, name="categories"),
]
