# Generated by Django 4.2.7 on 2023-11-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_category_name_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='news', to='news.tag'),
        ),
    ]
