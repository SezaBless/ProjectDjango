# Generated by Django 4.1 on 2022-09-13 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_certificate_portfolio"),
    ]

    operations = [
        migrations.DeleteModel(name="Certificate",),
        migrations.DeleteModel(name="Portfolio",),
        migrations.RemoveField(model_name="userprofile", name="skills",),
        migrations.DeleteModel(name="Skill",),
    ]