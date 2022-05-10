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


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


'''
class Get_Task_List(APIView):
    def get(self, request):
        task_list = Task.objects.all()
        serialized = TaskSerializer(task_list, many=True)
        return Response(serialized.data)



class TaskListAPI(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPI(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET', 'POST'])
def task_list_api(request, format=None):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
