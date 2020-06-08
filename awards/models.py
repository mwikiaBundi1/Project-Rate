from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField


import datetime as dt

Choices = (
    
    ('Python','Python'),
    ('php','PHP'),
    ('Java','Java'),
    ('c++','c++'),
    ('c#','c#'),
    




)



# Create your models here.
class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,categories):
        cls.objects.filter(categories=categories).delete()




class colors(models.Model):
    colors = models.CharField(max_length=100)

    def __str__(self):
        return self.colors

    def save_color(self):
        self.save()

    @classmethod
    def delete_color(cls,colors):
        cls.objects.filter(colors=colors).delete()


class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='landingpage/')
    description = HTMLField()
    link= models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    country = CountryField()
    technologies= MultiSelectField(choices = Choices)
    categories = models.ManyToManyField(categories)
    colors = models.ManyToManyField(colors)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls,search_term):
        # projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(colors__colors=search_term) | Q(technologies=search_term) | Q(categories__categories=search_term) | Q(country__countries=search_term))
        projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(country=search_term) | Q(overall_score__icontains=search_term))
        return projects


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
