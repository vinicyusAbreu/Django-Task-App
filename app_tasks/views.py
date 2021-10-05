from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def taskView(request):
    tasks = Task.objects.all().order_by('-id')
    
    return render(request, 'app_tasks/taskView.html', {'tasks': tasks})


@csrf_exempt
def newTask(request):
    if(request.POST['task'].strip() != ''):
        print(request.POST['task'])
        content = (request.POST['task'])
        create_object = Task.objects.create(title=content)
        print(create_object.id)

    return redirect('/')


def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/')


def clearTask(request):
    Task.objects.all().delete()
    print(Task)
    return redirect('/')


def searchTask(request):
    search = request.GET.get('filter')
    
    if search is None or not search:
        return redirect('/')
    
    qs = Q(title__icontains=search)

    print(Task.objects.filter(qs))
    tasks = Task.objects.filter(qs)
    print(tasks)
  

    return render(request, 'app_tasks/taskSearch.html', {'tasks': tasks})

def clearFilter(request):
    return redirect('/')

