import json
from django.db import models
from book.models import Book
from sistem_manajemen.models import Ruangan
from django.contrib.auth.models import User

class BookReport(models.Model):
    STATUS = [("UNDONE", "Undone"), ("SEMI-DONE", "Semi-done"), ("DONE", "Done")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    losts = models.TextField(blank=True, null=True)  # Store as JSON string
    brokens = models.TextField(blank=True, null=True)
    report_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS)
    message = models.CharField(blank=True, max_length=50)

    def set_losts(self, losts):
        self.losts = json.dumps(losts)

    def get_losts(self):
        return json.loads(self.losts)

    def set_brokens(self, brokens):
        self.brokens = json.dumps(brokens)

    def get_brokens(self):
        return json.loads(self.brokens)

class RoomReport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #new_room = models.OneToOneField(Ruangan, on_delete=models.CASCADE)
    report_date = models.DateField(auto_now_add=True)
    status = models.BooleanField()

class Complaint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    report_date = models.DateField(auto_now_add=True)
