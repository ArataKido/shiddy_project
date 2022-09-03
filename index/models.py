from django.db import models


class SocialLink(models.Model):
    """ Модель: Социальных сетей """
    title = models.CharField(verbose_name='Название', default='vk', max_length=2, help_text='Первые две буквы соц сети')
    link = models.URLField(verbose_name='Ссылка на социальную сеть')

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return f'Соц-сеть: {self.link}'
