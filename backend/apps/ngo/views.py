from rest_framework import generics, permissions, filters
from .models import NGO
from .serializers import NGOSerializer
from .permissions import IsOwnerOrReadOnly

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