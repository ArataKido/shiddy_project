from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import ContactForm


class Index(TemplateView):
    template_name = 'theme/pages/contact.html'


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index:index')
    else:
        form = ContactForm()

    return render(request, 'theme/pages/index.html', {'form': form})
