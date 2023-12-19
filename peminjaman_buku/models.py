# Create your models here.
from django.db import models
from django.contrib.auth.models import User 

class PinjamBuku(models.Model):
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)  
    buku = models.CharField(max_length=100) 
    tanggal_peminjaman = models.DateField()
    tanggal_pengembalian = models.DateField()
    status_acc = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pengguna.username} meminjam {self.buku}"


