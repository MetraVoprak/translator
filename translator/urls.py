"""translator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.index, name="index"),
    path("translator/", mainapp.translator, name="translator"),
    path("all_words/", include("mainapp.urls", namespace="all_words")),
    path("training/", mainapp.training, name="training"),
    path("auth", include("authnapp.urls", namespace="auth")),
    # ---
    # path("all_words/", mainapp.all_words, name="all_words"),
    # path("all_words/verb", mainapp.all_words, name='verb'),
    # path("all_words/noun", mainapp.all_words, name='noun'),
    # path("all_words/adjective", mainapp.all_words, name='adjective'),
    # path("all_words/pronoun", mainapp.all_words, name='pronoun'),
    # path("all_words/numerals", mainapp.all_words, name='numerals'),
    # path("all_words/adverb", mainapp.all_words, name='adverb'),
    # path('all_words/new_cat', mainapp.all_words, name='new_cat'),
    # ---
    # path('all_words/', include("mainapp.urls", namespace="all_words")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
