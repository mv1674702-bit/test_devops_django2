from django.shortcuts import render, redirect
from application.models import Task
# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_on = request.POST.get('created_on')
        deadline = request.POST.get('deadline')

        task = Task(title=title, description=description, created_on=created_on, deadline=deadline)
        task.save()
        
        return redirect('task')
    return render(request, 'home.html')

def taskDisplay(request):
    task = Task.objects.all()
    return render(request, 'taskdisplay.html',{'task':task})

def taskUpdate(request, id):
    task = Task.objects.get(pk = id)
    task.completed = True
    task.save()
    return redirect('task')

def taskDelete(request, id): 
    task = Task.objects.get(pk = id)
    task.delete()
    return redirect('task')
