# Generated by Django 4.2.6 on 2023-10-12 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AddField(
            model_name='events',
            name='photo',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='events',
            name='product_class',
            field=models.CharField(max_length=200, null=True, verbose_name='Класс'),
        ),
        migrations.AddField(
            model_name='events',
            name='type',
            field=models.CharField(max_length=200, null=True, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='events',
            name='weight',
            field=models.FloatField(null=True, verbose_name='Вес'),
        ),
    ]
