from django.db import models
from django.conf import settings
from camp.food.models import Food
from camp.food.models import Food

class Supplier(models.Model):
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', null=True)
    name = models.CharField(max_length=200, verbose_name='Наименование', null=True)
    category = models.CharField(max_length=200, verbose_name='Категория', null=True)
    create_date = models.DateTimeField()


    # def publish(self):
    #     self.edit_date = timezone.now()
    #     self.save()
    #
    def __str__(self):
        return self.name
