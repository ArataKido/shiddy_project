from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls', namespace='index')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('case/', include('case.urls', namespace='case')),
    path('social/', include('social.urls', namespace='social')),
    path('blog/', include('blog.urls', namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
