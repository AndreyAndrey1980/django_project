from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True)
    view_count = models.IntegerField(default=0)
    publicate = models.BooleanField(default=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField(null=True)
    create_date = models.DateTimeField(default=datetime.now)
    last_change_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
