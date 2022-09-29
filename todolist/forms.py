# from https://www.youtube.com/watch?v=EX6Tt-ZW0so

from django.forms import ModelForm
from todolist.models import Task

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']