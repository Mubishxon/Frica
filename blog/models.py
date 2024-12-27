from django.db import models
from django.urls import reverse
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Free(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='free/')

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='customer/')

    def __str__(self):
        return self.name

class Beauty(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='beauty/')

    def __str__(self):
        return self.name

class Kiyimlar(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='kiyimlar/')


    def __str__(self):
        return self.name
class Computer(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    price2 = models.IntegerField()
    img = models.ImageField(upload_to='computer/')
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("computerDetailView", args=[self.slug])

    def __str__(self):
        return self.name

