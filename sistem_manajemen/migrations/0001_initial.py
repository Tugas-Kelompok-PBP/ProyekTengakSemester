# Generated by Django 4.2.4 on 2023-12-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor', models.IntegerField()),
                ('ketersediaan', models.CharField(max_length=255)),
            ],
        ),
    ]
