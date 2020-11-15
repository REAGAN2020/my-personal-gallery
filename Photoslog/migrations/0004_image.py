# Generated by Django 3.1.3 on 2020-11-15 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Photoslog', '0003_auto_20201115_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='photos/')),
                ('Image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Photoslog.category')),
                ('Image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Photoslog.location')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
