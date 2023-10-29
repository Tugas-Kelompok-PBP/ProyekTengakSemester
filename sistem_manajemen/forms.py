from django import forms
from .models import Ruangan  # Import your Ruangan model

class RuanganForm(forms.ModelForm):
    class Meta:
        model = Ruangan  # Use your Ruangan model
        fields = ['nomor', 'ketersediaan']  # Define the fields you want in your form
