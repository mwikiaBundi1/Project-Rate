from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class categoriesTestClass(TestCase):
    def setUp(self):
        self.photos = categories(categories='Art')

    def test_instance(self):
        self.assertTrue(isinstance(self.photos,categories))

    def tearDown(self):
        categories.objects.all().delete()

    def test_save_method(self):
        self.photos.save_category()
        category = categories.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.photos.delete_category('photos')
        category = categories.objects.all()
        self.assertTrue(len(category)==0)

class colorsTestClass(TestCase):
    def setUp(self):
        self.Black = colors(colors='Black')

    def test_instance(self):
        self.assertTrue(isinstance(self.Black,colors))

    def tearDown(self):
        colors.objects.all().delete()

    def test_save_method(self):
        self.Black.save_color()
        color = colors.objects.all()
        self.assertTrue(len(color)>0)

    def test_delete_method(self):
        self.Black.delete_color('Black')
        color = colors.objects.all()
        self.assertTrue(len(color)==0)

