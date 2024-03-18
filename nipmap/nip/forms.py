from django import forms
from .models import Client, Project

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'assigned_users']