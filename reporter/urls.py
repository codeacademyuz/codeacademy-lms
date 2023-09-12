from django.urls import path
from .views import (
    AttemptView,
    ReporterView,
    ReporterByGroupName,
)

urlpatterns = [
    path('attempt/', AttemptView.as_view()),
    path('', ReporterView.as_view()),
    path('by-group/', ReporterByGroupName.as_view()),
]

