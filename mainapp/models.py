from django.db import models

# Create your models here.


class Part_of_speech(models.Model):
    name = models.CharField(verbose_name="имя части речи", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name


class Words(models.Model):
    category = models.ForeignKey(Part_of_speech, on_delete=models.CASCADE, default=0)
    eng_var = models.CharField(verbose_name="на английском", max_length=64, unique=True)
    rus_var = models.CharField(verbose_name="на русском", max_length=64, unique=True)

    def __str__(self):
        return f"{self.eng_var} ({self.category.name})"
