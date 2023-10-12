from django.db import models
from django.conf import settings


class Food(models.Model):
    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    section = models.CharField(max_length=200, verbose_name='Раздел', null=True)
    type = models.CharField(max_length=200, verbose_name='Вид/тип', null=True)
    name = models.CharField(max_length=200, verbose_name='Наименование', null=True)
    weight = models.FloatField(verbose_name='Вес', null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='images', null=True)


    # def publish(self):
    #     self.edit_date = timezone.now()
    #     self.save()
    #
    def __str__(self):
        return self.name
