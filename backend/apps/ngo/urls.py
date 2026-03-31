from django.urls import path # type: ignore
from .views import (
    NGOCreateView,
    NGOListView,
    NGODetailView,
    NGOUpdateView,
    NGODeleteView
)

urlpatterns = [
    path('create/', NGOCreateView.as_view()),
    path('', NGOListView.as_view()),
    path('<int:pk>/', NGODetailView.as_view()),
    path('<int:pk>/update/', NGOUpdateView.as_view()),
    path('<int:pk>/delete/', NGODeleteView.as_view()),
]