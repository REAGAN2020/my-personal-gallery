# Generated by Django 3.1.3 on 2020-11-15 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Photoslog', '0002_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='fname',
            new_name='name',
        ),
    ]