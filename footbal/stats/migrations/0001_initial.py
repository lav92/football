# Generated by Django 4.2.7 on 2023-12-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('tla', models.CharField(blank=True, max_length=50)),
                ('logo', models.CharField(blank=True, max_length=255)),
                ('data_football_id', models.IntegerField()),
            ],
        ),
    ]