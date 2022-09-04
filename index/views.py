from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import ContactForm
from .models import SocialLink, Answer, Product, ProductImage, PostBlog


class Index(ListView):
    """ Главная страница """
    template_name = 'index.html'

    def get(self, request):
        social_link = SocialLink.objects.all()
        answer = Answer.objects.all()
        work = Product.objects.all()

        context = {
            'social_link': social_link,
            'answer': answer,
            'work': work,
        }
        return render(request, self.template_name, context)


class PortfolioDetail(DetailView):
    """ Портфолио """
    template_name = 'portfolio-details.html'
    model = Product
    context_object_name = 'product'

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        product_image = ProductImage.objects.filter(product=pk)

        context = {
            'product': product,
            'product_image': product_image,
        }
        return render(request, self.template_name, context)


class Blog(ListView):
    template_name = 'blog.html'
    model = PostBlog
    paginate_by = 3
    context_object_name = 'post'


class BlogDetail(DetailView):
    template_name = 'blog-details.html'
    model = PostBlog
    context_object_name = 'post'


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index:index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
