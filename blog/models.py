from django.contrib.auth.models import User
from django.db import models


class PostBlog(models.Model):
    """ Модель: Пост в блог """
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Обложка', upload_to='media/blog/')
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    short_content = models.TextField(verbose_name='Короткое содержание')
    content = models.TextField(verbose_name='Содержимое поста')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Посты в блоге'
        verbose_name_plural = 'Посты в блоге'

    def __str__(self):
        return self.title
