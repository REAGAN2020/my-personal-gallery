from django.db import models
import datetime as dt
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    @classmethod
    def __str__(cls):
        return self.name
    

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        location = Location.objects.get(pk = id)
        return location

class Category(models.Model):
    name = models.CharField(max_length=50)
    @classmethod
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category
class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    Image = models.ImageField()
