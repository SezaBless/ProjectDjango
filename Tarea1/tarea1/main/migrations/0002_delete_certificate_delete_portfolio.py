# Generated by Django 4.1 on 2022-09-12 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Certificate",),
        migrations.DeleteModel(name="Portfolio",),
    ]
