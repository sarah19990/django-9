# Generated by Django 4.1.4 on 2023-02-22 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_issue'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Issue',
        ),
    ]
