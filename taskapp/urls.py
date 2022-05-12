from django.urls import path, include
from . import views
from .views import TaskViewSet, UserViewSet
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('api/', include(router.urls)),
    path('', views.index, name="index"),
    path('task_list', views.task_list, name="task_list"),
    path('table_practice', views.table_practice, name="table_practice"),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
