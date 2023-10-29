import json
from django.db import models
from book.models import Book
from sistem_manajemen.models import Ruangan
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def set_status(self, new_status):
        self.status = new_status

    def set_message(self, new_message):
        self.message = new_message

class Complaint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    report_date = models.DateField(auto_now_add=True)
