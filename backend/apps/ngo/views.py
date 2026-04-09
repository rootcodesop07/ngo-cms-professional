from rest_framework import generics, permissions, filters
from .models import NGO
from .serializers import NGOSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from apps.ngo.models import NGO


class NGOListCreateView(generics.ListCreateAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'name']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class NGODetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

from django.shortcuts import render

def home(request):
    from apps.ngo.models import NGO

    ngo_count = NGO.objects.count()
    total_donations = 0
    event_count = 0

    return render(request, 'home.html', {
        'ngo_count': ngo_count,
        'total_donations': total_donations,
        'event_count': event_count
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def dashboard(request):
    ngos = NGO.objects.all()
    return render(request, 'dashboard.html', {'ngos': ngos})