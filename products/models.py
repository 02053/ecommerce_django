from autoslug import AutoSlugField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='name')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Category'


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    marca = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    important = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Product'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        verbose_name_plural = 'Product Image'
