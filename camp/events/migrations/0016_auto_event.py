# Generated by Django 4.2.6 on 2023-10-12 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_auto_state_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0015_alter_product_event_product_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto_event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('auto_event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auto.auto', verbose_name='Еда')),
                ('events', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.events', verbose_name='Событие')),
            ],
            options={
                'verbose_name': 'Авто мобиль для события',
                'verbose_name_plural': 'Автомобили для событий',
            },
        ),
    ]
