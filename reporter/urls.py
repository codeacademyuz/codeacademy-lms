from django.urls import path
from .views import (
    AttemptView,
    ReporterView,
)

urlpatterns = [
    path('attempt/', AttemptView.as_view()),
    path('', ReporterView.as_view()),
]

