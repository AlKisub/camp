# Generated by Django 4.2.6 on 2023-10-12 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_alter_supplier_category'),
        ('product', '0003_remove_product_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier', verbose_name='Производитель'),
        ),
    ]