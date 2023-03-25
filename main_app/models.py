from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"


class Task(models.Model):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    PRIORITIES = (
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low")
    )
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=8, choices=PRIORITIES, default=MEDIUM, null=False)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker)

