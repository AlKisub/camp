# Generated by Django 4.2.6 on 2023-10-12 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_inventary_event_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventary_event',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]