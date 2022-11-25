from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Product, ProductImage


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


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
