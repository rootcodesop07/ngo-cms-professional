from django.urls import path
from .views import NGOListCreateView, NGODetailView

urlpatterns = [
    path('', NGOListCreateView.as_view(), name='ngo-list-create'),
    path('<int:pk>/', NGODetailView.as_view(), name='ngo-detail'),
]