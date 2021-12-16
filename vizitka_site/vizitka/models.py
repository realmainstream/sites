from django.db import models


class client(models.Model):
    name = models.CharField('Имя', max_length=50)
    task = models.TextField('Желание')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
