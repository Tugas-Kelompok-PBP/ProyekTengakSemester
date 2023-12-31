# Generated by Django 4.2.6 on 2023-10-26 19:01

from django.db import migrations
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "data_buku.json")


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_ketersediaan_book_vip'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]
