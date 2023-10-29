from django.db import models


# Create your models here.

class fitur_premium(models.Model):
    title = models.TextField(null=True, blank=True)
    jumlah_hari = models.TextField(null=True, blank=True)
    id_user = models.TextField(null=True, blank=True)