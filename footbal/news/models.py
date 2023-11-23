from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, verbose_name='url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='news', null=True)

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('single', kwargs={'news_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(blank=True, upload_to='category/')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.description
