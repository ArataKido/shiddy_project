from django.db import models

# Портфолио
class Product(models.Model):
    """ Модель: Наши работы """
    image = models.ImageField(verbose_name='Обложка', upload_to='media/portfolio')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    pricer = models.CharField(verbose_name='Заказчик', max_length=100)

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