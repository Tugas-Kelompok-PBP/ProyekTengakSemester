from django.db import models
from book.models import Book
from django.contrib.auth.models import User

class BookReport(models.Model):
    STATUS = [("UNDONE", "Undone"), ("SEMI-DONE", "Semi-done"), ("DONE", "Done")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    losts = models.JSONField(default=list, blank=True)
    brokens = models.JSONField(default=list, blank=True)
    report_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS)
    message = models.CharField(blank=True, max_length=50)

class RoomReport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    new_room = None
    cancel = models.BooleanField(default=False)
    report_date = models.DateField(auto_now_add=True)
    status = models.BooleanField()

class Complaint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    report_date = models.DateField(auto_now_add=True)