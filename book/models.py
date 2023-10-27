from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    ketersediaan = models.TextField(null=True, blank=True)
    vip = models.TextField(null=True, blank=True)