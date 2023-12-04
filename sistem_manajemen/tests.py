from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from sistem_manajemen.models import Ruangan
from book.models import Book
from peminjaman_buku.models import PinjamBuku
from .forms import RuanganForm

class SistemManajemenViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='test-pekerja', password='test-password')

        # Create some sample data for testing
        self.ruangan = Ruangan.objects.create(nama='Ruangan A', ketersediaan='tersedia')
        self.book = Book.objects.create(title='Book A', genre='Fiction', ketersediaan='tersedia')
        self.pinjam_buku = PinjamBuku.objects.create(tanggal_peminjaman='2023-01-01', tanggal_pengembalian='2023-01-10')

    def test_show_sistem_view(self):
        # Log in the user
        self.client.login(username='test-pekerja', password='test-password')

        # Make a GET request to the view
        response = self.client.get(reverse('sistem_manajemen:show_sistem'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_show_sistem_ruangan_view(self):
        self.client.login(username='test-pekerja', password='test-password')
        response = self.client.get(reverse('sistem_manajemen:show_sistem_ruangan'))
        self.assertEqual(response.status_code, 200)

    # Add more test cases for other views similarly

    def test_ganti_status_ketersediaan_view(self):
        self.client.login(username='test-pekerja', password='test-password')
        response = self.client.get(reverse('sistem_manajemen:ganti_status_ketersediaan', args=(self.ruangan.pk,)))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect response

    def test_ganti_status_peminjaman_view(self):
        self.client.login(username='test-pekerja', password='test-password')
        response = self.client.get(reverse('sistem_manajemen:ganti_status_peminjaman', args=(self.pinjam_buku.pk,)))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect response

    # Add more test cases for other views similarly
