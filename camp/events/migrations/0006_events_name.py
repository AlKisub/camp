# Generated by Django 4.2.6 on 2023-10-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_events_photo_remove_events_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
    ]
