from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})
    # return render(request, 'bas.html')

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('task_title')
        Task.objects.create(title=title)
    return redirect('api:index')
