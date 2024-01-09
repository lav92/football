# Generated by Django 5.0 on 2024-01-07 11:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.SmallIntegerField(db_index=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.goods')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]