from django.urls import path

from .views import StudentView, GroupView

urlpatterns = [
    path('', StudentView.as_view()),
    path('<int:pk>/', StudentView.as_view()),
    path('groups/', GroupView.as_view()),
]
