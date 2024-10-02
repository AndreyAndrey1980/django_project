from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField(null=True)
    create_date = models.DateTimeField(default=datetime.now)
    last_change_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name
