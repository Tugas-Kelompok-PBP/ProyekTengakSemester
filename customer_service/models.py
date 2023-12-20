import json
from django.db import models
from book.models import Book
from sistem_manajemen.models import Ruangan
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=500, default="Aninom")
    losts = models.TextField(blank=True, null=True)
    brokens = models.TextField(blank=True, null=True)
    report_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=12)
    message = models.TextField()

    def set_losts(self, losts):
        self.losts = json.dumps(losts)

    def get_losts(self):
        return json.loads(self.losts)

    def set_brokens(self, brokens):
        self.brokens = json.dumps(brokens)

    def get_brokens(self):
        return json.loads(self.brokens)

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=500, default="Anonim")
    description = models.TextField()
    report_date = models.DateField(auto_now_add=True)
    isRead = models.BooleanField(default=False)