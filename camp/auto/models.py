from django.db import models
from django.conf import settings


class Auto(models.Model):
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    name = models.CharField(max_length=200, verbose_name='Марка/модель', null=True)
    product_class = models.CharField(max_length=200, verbose_name='Класс', null=True)
    type = models.CharField(max_length=200, verbose_name='Тип кузова', null=True)
    trunk_volume = models.CharField(max_length=200, verbose_name='Объём багажника', null=True)
    state_number = models.CharField(max_length=9, verbose_name='Номер', null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='images', null=True)

    # def publish(self):
    #     self.edit_date = timezone.now()
    #     self.save()
    #
    def __str__(self):
        return self.name
