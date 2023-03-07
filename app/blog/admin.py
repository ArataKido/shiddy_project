from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import PostBlog, Category


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PostBlog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


admin.site.register(PostBlog, BlogAdmin)
admin.site.register(Category)