from django.contrib.auth import get_user_model
from apps.core.models import ModelBase
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

User = get_user_model()

# Create your models here.
class Category(ModelBase):
    name = models.CharField(verbose_name='Name', max_length=50, unique=True)
    image = models.ImageField(verbose_name='Image', upload_to='categories', null=True, blank=True)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return self.image.url
        return '/static/img/default-category.png'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        db_table = 'categories'


class Product(ModelBase):
    name = models.CharField(verbose_name='Name', max_length=50, unique=True)
    image = models.ImageField(verbose_name='Image', upload_to='products', null=True, blank=True)
    description = CKEditor5Field(verbose_name="Description", null=True, blank=True, config_name='extends')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    stock = models.PositiveIntegerField(verbose_name='Stock', default=0)
    categories = models.ManyToManyField('Category', related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return self.image.url
        return '/static/img/default-product.png'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'