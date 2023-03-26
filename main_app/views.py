from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from main_app.models import Task, Worker


def index(request):
    return render(request, "main_app/index.html")


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task


class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = Worker
