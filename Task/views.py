from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Task
from . forms import TaskForm
# Create your views here.

def home(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'Task/home.html', context)

class TaskListView(ListView):
    model = Task
    template_name = 'Task/home.html'
    context_object_name = 'tasks'
    ordering = ['-due_date']

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'Task/task_form.html'
    success_url = reverse_lazy('task-home')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-home')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-home')