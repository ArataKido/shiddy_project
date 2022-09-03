from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import SocialLink


class Index(ListView):
    """ Главная страница """
    template_name = 'index.html'

    def get(self, request):
        social_link = SocialLink.objects.all()

        context = {
            'social_link': social_link
        }
        return render(request, self.template_name, context)


class Blog(TemplateView):
    template_name = 'blog.html'
