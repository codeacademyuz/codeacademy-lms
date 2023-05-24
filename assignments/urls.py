from django.urls import path

from .views import AssignmentView, TaskView, TaskByAssignmentView

urlpatterns = [
    path('', AssignmentView.as_view()),
    path('<int:pk>/', AssignmentView.as_view()),
    path('task/', TaskView.as_view()),
    path('task/<int:pk>/', TaskView.as_view()),
    path('<int:assignment_id>/tasks/', TaskByAssignmentView.as_view()),
]
