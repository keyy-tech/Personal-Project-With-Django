from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('create/',views.createTask, name='create_task'),
    path('read/',views.readTasks, name= 'read_tasks'),
    path('update/<int:id>/',views.updateTask, name='update_task'),
    path('delete/<int:id>/',views.deleteTask, name='delete_task')
]
