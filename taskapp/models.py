from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField('Task Name', max_length=1000)
    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(
        'Completed Date', blank=True, null=True)
    due_date = models.DateTimeField("Due Date", blank=True, null=True)

    def __str__(self):
        return self.name
