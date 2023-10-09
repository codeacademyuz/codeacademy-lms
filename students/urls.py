from django.urls import path

from .views import StudentView, GroupView, CourseView, HomeworkView

urlpatterns = [
    path('students/', StudentView.as_view()),
    path('students/<int:pk>/', StudentView.as_view()),
    path('courses/', CourseView.as_view()),
    path('courses/<int:pk>/groups/', GroupView.as_view()),
    path('courses/<int:assignment_id>/groups/<int:group_id>/homeworks/', HomeworkView.as_view()),
]
