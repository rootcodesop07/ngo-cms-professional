from django.urls import path
from .views import NGOCreateView

urlpatterns = [
    path('create/', NGOCreateView.as_view(), name='ngo-create'),
]