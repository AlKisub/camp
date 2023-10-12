# Generated by Django 4.2.6 on 2023-10-12 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0007_alter_events_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventary_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('inventary_event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory', verbose_name='Инвентарь')),
            ],
            options={
                'verbose_name': 'Инвентарь для события',
                'verbose_name_plural': 'Инвентарь для событий',
            },
        ),
    ]
