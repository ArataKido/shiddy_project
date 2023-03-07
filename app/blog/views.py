from django.views.generic import DetailView, ListView
from blog.models import PostBlog, Category


class BlogAll(ListView):
    template_name = 'theme/pages/blog-standard.html'
    model = PostBlog
    paginate_by = 3
    context_object_name = 'post'


class BlogDetail(DetailView):
    template_name = 'theme/pages/detail/blog-single.html'
    model = PostBlog
    context_object_name = 'post'

class BlogCategory(DetailView):
    template_name = 'theme/pages/blog-category.html'
    model = Category
    context_object_name = 'post'
