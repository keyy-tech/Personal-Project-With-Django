from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    return render(request, "ToDoList/index.html")


# Create task
def createTask(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("read_tasks")
    context = {"form": form}
    return render(request, "ToDoList/create_task.html", context)


# Read tasks
def readTasks(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "ToDoList/read_tasks.html", context)


# Update task
def updateTask(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "ToDoList/update_task.html", context)


# Delete task
def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return render(request, "ToDoList/delete_task.html")
