from django.db import models


class Answer(models.Model):
    """ Модель: Отзывы клиентов """
    image = models.ImageField(upload_to='media/', verbose_name='Фото отзыва')
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    content = models.TextField(verbose_name='Описание')
    full_name = models.CharField(verbose_name="Ф И О", max_length=250)
    company = models.CharField(verbose_name='Название компании', max_length=250)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзыв'

    def __str__(self):
        return f'Отзыв: {self.title} от компании {self.company}'


class Contact(models.Model):
    """ Модель: Форма обратной связи """
    full_name = models.CharField(verbose_name='Ф И О ', max_length=300)
    email = models.CharField(verbose_name='Email', max_length=300)
    phone = models.CharField(verbose_name='Номер телефона', max_length=50)
    content = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная свзь'

    def __str__(self):
        return f'Запрос на связь: {self.full_name} номер: {self.phone}'
