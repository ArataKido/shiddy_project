from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify





class PostBlog(models.Model):
    """ Модель: Пост в блог """

    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image', upload_to='media/blog/')
    title = models.CharField(verbose_name="Title", max_length=100)
    short_content = models.TextField(verbose_name='short description')
    content = models.TextField(verbose_name='content')
    date = models.DateField(auto_now_add=True)
    keyword = models.CharField(max_length=100, verbose_name='keywords for SEO')
    description = models.CharField(max_length=100, verbose_name='description for SEO')
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=False, default=slugify(title), verbose_name='Ссылка')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'

    def get_absolute_url(self, **kwargs):
        return f'/post/{self.slug}'

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=100)
    blog = models.ManyToManyField(PostBlog, default=None )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name