from django.forms import ModelForm, ValidationError
from beranda.book import Book

class ProductForm(ModelForm):
    class Meta:
        model = Book
        fields = ["book"]