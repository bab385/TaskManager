from .models import Task
from django.contrib.auth.models import User
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        # fields = ['name', 'created_date', 'created_by',
        # 'completed', 'completed_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
