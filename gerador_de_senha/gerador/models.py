from django.db import models

class Cadeado(models.Model):
    site = models.CharField(max_length=8000)
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
