from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.


class Goods(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='goods/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True, db_index=True)

    def __str__(self):
        return f'{self.pk} {self.name} {self.price}'

    def get_absolute_url(self):
        return reverse('add-to-cart', kwargs={'goods_slug': self.slug})

    class Meta:
        ordering = ['price']
        verbose_name = "Товар"
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = "Категория товаров"
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('shop:goods_category', kwargs={'cat_slug': self.slug})


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    session_key = models.CharField(max_length=100, null=True, blank=True)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(db_index=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.goods} {self.quantity}'


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    goods_list = models.JSONField()
    delivery = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    delivery_date = models.DateField()

    def __str__(self):
        return f'{self.user} {self.created_at} {self.goods_list}'
