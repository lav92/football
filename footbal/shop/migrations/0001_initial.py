# Generated by Django 5.0 on 2024-01-06 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'verbose_name_plural': 'Категории товаров',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='goods/%Y/%m/%d')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['price'],
            },
        ),
    ]