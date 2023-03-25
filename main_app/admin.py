from django.contrib import admin
from main_app.models import Worker, Position, TaskType, Task

admin.site.register(Worker)
admin.site.register(Position)
admin.site.register(Task)
admin.site.register(TaskType)
