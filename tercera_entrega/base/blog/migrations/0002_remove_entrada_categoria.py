# Generated by Django 4.2.7 on 2023-12-05 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='categoria',
        ),
    ]
