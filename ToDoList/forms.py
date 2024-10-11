from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        # labels
        labels = {
            'title': 'Task',
            'completed': 'Completed',
            'description': 'Description'
        }

        # widgets
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add new task...', 'class': 'form-control'}),
            'completed': forms.CheckboxInput(),
            'description': forms.Textarea(attrs={'placeholder': 'Add description...', 'class': 'form-control'}),
        }