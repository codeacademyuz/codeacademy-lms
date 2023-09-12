from django.urls import path
from .views import (
    AttemptView,
    ReporterByGroupName,
)

urlpatterns = [
    path('attempt/', AttemptView.as_view()),
    path('by-group/', ReporterByGroupName.as_view()),
]

