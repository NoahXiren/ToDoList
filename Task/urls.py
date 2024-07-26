from django.urls import path
from . import views
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name="task-home"),
    path('task/<int:pk>/',TaskDetailView.as_view(), name='task-detail'),
    path('task/create/',TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/',TaskUpdateView.as_view(), name='task-update'),    
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(), name='task-delete'),    
]
