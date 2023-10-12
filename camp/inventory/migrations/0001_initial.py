# Generated by Django 4.2.6 on 2023-10-12 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_class', models.CharField(max_length=200, null=True, verbose_name='Класс')),
                ('type', models.CharField(max_length=200, null=True, verbose_name='Тип')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('weight', models.FloatField(null=True, verbose_name='Вес')),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
                ('photo', models.ImageField(null=True, upload_to='images', verbose_name='Фото')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Инвентарь',
                'verbose_name_plural': 'Инвентарь',
            },
        ),
    ]
