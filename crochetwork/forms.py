from django import forms
from .models import Category
from .models import Entry


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_description']
        """
                labels = {'project_name': '',
                  'project_description': '',
                  'start_date, ''}
        """


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_name', 'entry_image']