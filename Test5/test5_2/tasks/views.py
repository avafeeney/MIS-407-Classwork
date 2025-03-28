from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from tasks.models import Task
from tasks.forms import TaskCreateForm


class TaskListView(ListView):
    model = Task
    template_name = 'task_index.html'
    context_object_name = 'tasks'
    ordering = ['done', '-priority']


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(CreateView):
    template_name = 'task_create_form.html'
    form_class = TaskCreateForm

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_update_form.html'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy("task:index")
