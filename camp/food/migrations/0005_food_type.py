# Generated by Django 4.2.6 on 2023-10-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_remove_food_quantity_remove_food_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.CharField(max_length=200, null=True, verbose_name='Вид/тип'),
        ),
    ]