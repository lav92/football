from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, verbose_name='url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    views = models.IntegerField(default=0)
