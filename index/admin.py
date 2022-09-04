from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
from index.models import SocialLink, Product, Contact, Answer, ProductImage, Category, PostBlog


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductImageAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    form = PostAdminForm


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PostBlog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PostBlog, BlogAdmin)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(Contact)
