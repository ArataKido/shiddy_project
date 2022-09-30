from django.shortcuts import render
from django.views.generic import DetailView, ListView

from portfolio.models import Product, ProductImage


class Portfolio(ListView):
    template_name = 'theme/pages/portfolio.html'
    model = Product
    context_object_name = 'products'


class PortfolioDetail(DetailView):
    """ Портфолио """
    template_name = 'theme/pages/detail/portfolio-single.html'
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