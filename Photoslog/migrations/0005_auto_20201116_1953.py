# Generated by Django 3.1.3 on 2020-11-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photoslog', '0004_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
