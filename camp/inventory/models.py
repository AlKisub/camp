from django.db import models
from django.conf import settings


class Inventory(models.Model):
    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Инвентарь'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    product_class = models.CharField(max_length=200, verbose_name='Класс', null=True)
    type = models.CharField(max_length=200, verbose_name='Тип', null=True)
    name = models.CharField(max_length=200, verbose_name='Название', null=True)
    weight = models.FloatField(verbose_name='Вес', null=True)
    price = models.FloatField(verbose_name='Цена', null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='images', null=True)


    # def publish(self):
    #     self.edit_date = timezone.now()
    #     self.save()
    #
    def __str__(self):
        return self.name
