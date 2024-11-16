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
    user_email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            ("set_false_product_published_status", "Can cancel publicate product"),
            ("change_product_description", "Can change product description"),
            ("change_product_category", "Can change product category")
        ]


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True)
    view_count = models.IntegerField(default=0)
    publicate = models.BooleanField(default=True)
    text = models.TextField()
    create_date = models.DateTimeField(default=datetime.now)
    last_change_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.title


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    version_name = models.CharField(max_length=100)
    version_number = models.CharField(max_length=10)
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return self.version_number

    class Meta:
        ordering = ('version_number',)
