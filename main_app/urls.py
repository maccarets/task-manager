from django.urls import path

from main_app.views import index, TasksListView, WorkersListView

urlpatterns = [
    path("", index, name="index"),
    path("tasks", TasksListView.as_view(), name="task-list"),
    path("workers", WorkersListView.as_view(), name="worker-list")
]

app_name = "main_app"
