from django.contrib.auth.models import User
from django.db import models


# Ссылки на нас
class SocialLink(models.Model):
    """ Модель: Социальных сетей """
    title = models.CharField(verbose_name='Название', default='vk', max_length=2, help_text='Первые две буквы соц сети')
    link = models.URLField(verbose_name='Ссылка на социальную сеть')

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return f'Соц-сеть: {self.link}'


# Отзывы
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


# Категории
class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'


# Портфолио
class Product(models.Model):
    """ Модель: Наши работы """
    image = models.ImageField(verbose_name='Обложка', upload_to='media/portfolio')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    pricer = models.CharField(verbose_name='Заказчик', max_length=100)
    category = models.ManyToManyField(Category, verbose_name='Категория')

    class Meta:
        verbose_name = 'Наши работы'
        verbose_name_plural = 'Наши работы'

    def __str__(self):
        return f'Работа: {self.title}'


# Галерея
class ProductImage(models.Model):
    """ Модель: Альбом работ """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/portfolio/')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return f'Картинка: {self.image.path} |  в работе {self.product.title}'


# Обратная связь
class Contact(models.Model):
    """ Модель: Форма обратной связи """
    Type = (
        (0, 'Графический дизайн'),
        (1, 'Разработка сайта'),
        (2, 'Администрирование сервера'),
        (3, 'SEO')
    )
    full_name = models.CharField(verbose_name='Ф И О ', max_length=300)
    email = models.CharField(verbose_name='Email', max_length=300)
    phone = models.CharField(verbose_name='Номер телефона', max_length=50)
    type_project = models.IntegerField(verbose_name='Тип проекта', choices=Type)
    content = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная свзь'

    def __str__(self):
        return f'Запрос на связь: {self.full_name} номер: {self.phone}'


""" Блок блога """


class PostBlog(models.Model):
    """ Модель: Пост в блог """
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Обложка', upload_to='media/blog/')
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    short_content = models.TextField(verbose_name='Короткое содержание')
    content = models.TextField(verbose_name='Содержимое поста')
    date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category, verbose_name='Категории')
