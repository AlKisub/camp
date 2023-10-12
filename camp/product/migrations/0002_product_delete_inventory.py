# Generated by Django 4.2.6 on 2023-10-12 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supplier', '0002_alter_supplier_category'),
        ('food', '0006_remove_food_price'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Наименование')),
                ('weight', models.FloatField(null=True, verbose_name='Вес')),
                ('create_date', models.DateTimeField()),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food', verbose_name='Еда')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
