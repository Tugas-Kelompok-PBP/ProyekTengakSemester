from django.db import models
from book.models import Book
# Create your models here.
class UserReview(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    rating = models.IntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.user_name} for {self.book.title}"