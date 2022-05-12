from django.shortcuts import render
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from taskapp import serializers
from taskapp.serializers import TaskSerializer, UserSerializer
from .models import Task
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from datetime import date


def index(request):
    return render(request, 'taskapp/index.html', {})


@csrf_protect
def task_list(request):
    tasks = Task.objects.all()
    today = date.today()
    current_date = today.strftime("%Y-%m-%d")
    print(current_date)
    return render(request, 'taskapp/task_list.html', {
        'tasks': tasks,
        'current_date': current_date,
    })


def table_practice(request):
    tasks = Task.objects.all()
    today = date.today()
    return render(request, 'taskapp/table_practice.html', {
        'tasks': tasks,
        'today': today,
    })


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
