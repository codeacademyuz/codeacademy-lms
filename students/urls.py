from django.urls import path

from .views import StudentView, StudentByRegionView

urlpatterns = [
    path('/', StudentView.as_view()),
    path('/<int:pk>/', StudentView.as_view()),
    path('/region/<int:region_id>/', StudentByRegionView.as_view()),
]
