from django import forms
from .models import Project
from .models import Entry


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_description']
        """
                labels = {'project_name': '',
                  'project_description': '',
                  'start_date, ''}
        """


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_name']