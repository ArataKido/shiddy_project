from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from case.models import Case


class CaseAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Case
        fields = '__all__'


class CaseAdmin(admin.ModelAdmin):
    form = CaseAdminForm


admin.site.register(Case, CaseAdmin)
