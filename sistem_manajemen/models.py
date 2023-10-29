from django.db import models

class Ruangan(models.Model):
    nomor = models.IntegerField()
    ketersediaan = models.CharField(max_length=255)