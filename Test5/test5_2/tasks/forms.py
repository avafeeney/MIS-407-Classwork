from django import forms
from tasks.models import Task

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
