from django.urls import path
from .views import *

urlpatterns = [path('', taskView, name='task_view'),
               path('newTask/', newTask, name='new_task'),
               path('delete/<int:id>', deleteTask, name='delete_task'),
               path('deleteAll/', clearTask, name='clear_task'),
               path('search/', searchTask, name='search_task'),
               path('clearFilter/', clearFilter, name="clear_filter")
               ]
