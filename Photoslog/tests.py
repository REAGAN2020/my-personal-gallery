from django.test import TestCase
from .models import Location,Category

# Create your tests here.

class LocationTestClass(TestCase):
    #Setup Method
    def setUp(self):
        self.loc = Location(name="Nairobi")
        self.loc.save_location()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))
    
    def test_save_method(self):
        self.loc.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
    
    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.loc.id)
        location.update_location('Nairobi')
        location  = Location.get_location_id(self.loc.id)
        self.assertTrue(location.name == 'Nairobi')

class CategoryTestClass(TestCase):
    #setup Method
    def setUp(self):
        self.teflon = Category(name="designs")
        self.teflon.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.teflon, Category))

    def test_save_method(self):
        self.teflon.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.teflon.save_category()
        self.teflon.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.teflon.id)
        category.update_category('Fashion')
        category = Category.get_category_id(self.teflon.id)
        self.assertTrue(category.name == 'Fashion')
    
