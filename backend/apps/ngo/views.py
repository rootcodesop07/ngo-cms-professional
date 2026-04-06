from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import NGO
from .serializers import NGOSerializer

# ✅ CREATE
class NGOCreateView(generics.CreateAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# ✅ LIST + SEARCH + FILTER + PAGINATION
class NGOListView(generics.ListAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer
    permission_classes = [IsAuthenticated]

    # 🔥 FILTER + SEARCH
    filterset_fields = ['name']
    search_fields = ['name', 'description']


# ✅ UPDATE
class NGOUpdateView(generics.UpdateAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer
    permission_classes = [IsAuthenticated]


# ✅ DELETE
class NGODeleteView(generics.DestroyAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer
    permission_classes = [IsAuthenticated]