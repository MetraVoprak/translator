# Generated by Django 3.2.16 on 2023-03-14 15:11

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Load model for make changes
    word_model = apps.get_model("mainapp", "Words")
    # Load model for make changes
    cat_model = apps.get_model("mainapp", "Part_of_speech")

    cat_obj = cat_model.objects.create(pk=1, name="verb", description="глагол")

    word_model.objects.create(pk=1, category=cat_obj, eng_var="run", rus_var="бежать")
    word_model.objects.create(pk=2, category=cat_obj, eng_var="jump", rus_var="прыгать")

    del cat_obj

    cat_obj = cat_model.objects.create(pk=2, name="noun", description="существительное")

    word_model.objects.create(pk=3, category=cat_obj, eng_var="animal", rus_var="животное")
    word_model.objects.create(pk=4, category=cat_obj, eng_var="book", rus_var="книга")

    del cat_obj

    cat_obj = cat_model.objects.create(pk=3, name="adjective", description="прилагательное")

    word_model.objects.create(pk=5, category=cat_obj, eng_var="big", rus_var="большой")
    word_model.objects.create(pk=6, category=cat_obj, eng_var="dirty", rus_var="грязный")

    del cat_obj

    cat_obj = cat_model.objects.create(pk=4, name="pronoun", description="местоимение")

    word_model.objects.create(pk=7, category=cat_obj, eng_var="he", rus_var="он")
    word_model.objects.create(pk=8, category=cat_obj, eng_var="they", rus_var="они")

    del cat_obj

    cat_obj = cat_model.objects.create(pk=5, name="numerals", description="числительное")

    word_model.objects.create(pk=9, category=cat_obj, eng_var="first", rus_var="первый")
    word_model.objects.create(pk=10, category=cat_obj, eng_var="two", rus_var="два")

    del cat_obj

    cat_obj = cat_model.objects.create(pk=6, name="adverb", description="наречие")

    word_model.objects.create(pk=11, category=cat_obj, eng_var="beautifully", rus_var="красиво")
    word_model.objects.create(pk=12, category=cat_obj, eng_var="easily", rus_var="просто")

    del cat_obj


def revers_func(apps, shema_editor):
    word_model = apps.get_model("mainapp", "Words")
    cat_model = apps.get_model("mainapp", "Part_of_speech")

    word_model.objects.all().delete()
    cat_model.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0002_auto_20230213_1438"),
    ]

    operations = [migrations.RunPython(forwards_func)]