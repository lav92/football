from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    slug = models.SlugField(max_length=200, verbose_name='url', unique=True)
    # content = models.TextField(blank=True, verbose_name='Текст статьи')
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Титульное фото')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='news', null=True,
                                 verbose_name='Категория')
    tag = models.ManyToManyField('Tag', blank=True, related_name='tags', verbose_name='Тег')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='author_news',
                               verbose_name='Автор')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('single', kwargs={'news_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(blank=True, upload_to='category/')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.description


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = "Тег"
        verbose_name_plural = 'Теги'
