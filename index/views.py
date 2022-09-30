from django.views.generic import TemplateView
from case.models import Case
from portfolio.models import Product
from social.models import Answer
from blog.models import PostBlog


class Index(TemplateView):
    """ Главная страница """
    template_name = 'theme/pages/index.html'

    def get_context_data(self, **kwargs):
        portfolio = Product.objects.order_by('-id')
        cases = Case.objects.order_by('-id')
        answers = Answer.objects.order_by('-id')
        posts = PostBlog.objects.order_by('-id')

        context = {
            'portfolio': portfolio,
            'cases': cases,
            'answers': answers,
            'posts': posts
        }
        return context