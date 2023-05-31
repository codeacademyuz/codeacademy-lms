from django.urls import path
from .views import (
    AttemptView,
    ReporterView,
    ReporterByRegion,
    ReporterByGroupName,
)

urlpatterns = [
    path('attempt/', AttemptView.as_view()),
    path('', ReporterView.as_view()),
    path('by-region/', ReporterByRegion.as_view()),
    path('by-group/', ReporterByGroupName.as_view()),
]

