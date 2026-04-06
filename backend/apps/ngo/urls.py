from django.urls import path # type: ignore
from .views import (
    NGOCreateView,
    NGOListView,
    NGOUpdateView,
    NGODeleteView
)

urlpatterns = [
    path('', NGOListView.as_view()),
    path('create/', NGOCreateView.as_view()),
    path('<int:pk>/update/', NGOUpdateView.as_view()),
    path('<int:pk>/delete/', NGODeleteView.as_view()),
]