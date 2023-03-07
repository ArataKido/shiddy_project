from django.db import models


class Case(models.Model):
    """
    Кейсы нашей студии, содержат готовые решения
    """
    image = models.ImageField(upload_to='media/', verbose_name='Миниатюра')
    category = models.CharField(verbose_name='Категории', max_length=900)
    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description = models.TextField(verbose_name='Содержимое')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Кейсы готовых решений'
        verbose_name_plural = 'Кейсы готовых решений'

    def __str__(self):
        return self.title
