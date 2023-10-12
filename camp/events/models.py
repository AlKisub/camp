from django.db import models
from django.conf import settings
from camp.inventory.models import Inventory
from camp.product.models import Product
from camp.auto.models import Auto
from django.db.models.signals import post_save, post_delete, pre_save

class Events(models.Model):
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    type = models.CharField(max_length=200, verbose_name='Тип', null=True)
    name = models.CharField(max_length=200, verbose_name='Название', null=True)
    event_date = models.DateTimeField(verbose_name='Дата события', null=True)
    create_date = models.DateTimeField(verbose_name='Дата создания', null=True)

    def __str__(self):
        return self.name

class Inventary_event(models.Model):
    class Meta:
        verbose_name = 'Инвентарь для события'
        verbose_name_plural = 'Инвентарь для событий'

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    events = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Событие', null=True)
    inventary_event = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name='Инвентарь', null=True)

    def __str__(self):
        return self.inventary_event.name

class Product_event(models.Model):
    class Meta:
        verbose_name = 'Продукты для события'
        verbose_name_plural = 'Продукты для событий'

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    events = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Событие', null=True)
    product_event = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Еда', null=True)
    quantity = models.IntegerField(verbose_name='Количество', null=True)
    total = models.FloatField(verbose_name='Сумма', null=True, blank=True)

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        instance.total = round(instance.quantity * instance.product_event.price, 2)

    def __str__(self):
        return self.product_event.name
class Auto_event(models.Model):
    class Meta:
        verbose_name = 'Авто мобиль для события'
        verbose_name_plural = 'Автомобили для событий'

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    events = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Событие', null=True)
    auto_event = models.ForeignKey(Auto, on_delete=models.CASCADE, verbose_name='Еда', null=True)


    # def publish(self):
    #     self.edit_date = timezone.now()
    #     self.save()
    #
    def __str__(self):
        return self.auto_event.name


pre_save.connect(Product_event.pre_save, Product_event, dispatch_uid="camp.events.models.Product_event")