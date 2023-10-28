from django.forms import ModelForm
from ulasan.models import UserReview

class BookForm(ModelForm):
    class Meta:
        model = UserReview
        fields = ['user_name', 'rating', 'review_text'] 