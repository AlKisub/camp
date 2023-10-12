from django.db import models
from django.conf import settings
from camp.food.models import Food
from camp.supplier.models import Supplier
from camp.retailer.models import Retailer

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Еда')
    name = models.CharField(max_length=200, verbose_name='Наименование', null=True)
    weight = models.FloatField(verbose_name='Вес', null=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, verbose_name='Продавец', null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Производитель', null=True)
    create_date = models.DateTimeField()
    price = models.FloatField(verbose_name='Цена', null=True)

    def __str__(self):
        return self.name
    # def publish(self):
    #     self.edit_date = timezone.now()
    #     self.save()
    #
    # def __str__(self):
    #     return self.subject
