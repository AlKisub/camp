# Generated by Django 4.2.6 on 2023-10-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_product_event_delete_food_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_event',
            options={'verbose_name': 'Продукты для события', 'verbose_name_plural': 'Протукты для событий'},
        ),
        migrations.AlterField(
            model_name='product_event',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
