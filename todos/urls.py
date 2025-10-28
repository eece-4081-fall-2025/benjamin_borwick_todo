from django.urls import path
from .views import task_create, task_list

urlpatterns = [
    path("", task_list, name="task_list"),
    path("tasks/new/", task_create, name="task_create"),
]