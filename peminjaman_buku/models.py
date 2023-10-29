# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Jika Anda menggunakan User model bawaan Django

class PinjamBuku(models.Model):
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)  # Menggunakan ForeignKey untuk menghubungkan dengan pengguna
    buku = models.CharField(max_length=100)  # Ganti ini dengan model buku yang sesuai jika Anda memiliki model Buku terpisah
    tanggal_peminjaman = models.DateField()
    tanggal_pengembalian = models.DateField()
    status_acc = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pengguna.username} meminjam {self.buku}"


