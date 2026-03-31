from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from .models import NGO
from .serializers import NGOSerializer

class NGOCreateView(APIView): # Day 8: List & Detail APIs implemented
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = NGOSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({
                "message": "NGO created successfully",
                "data": serializer.data
            })

        return Response(serializer.errors)
    

class NGOListView(APIView):
     permission_classes = [IsAuthenticated]

     def get(self, request):
        ngos = NGO.objects.filter(created_by=request.user)
        serializer = NGOSerializer(ngos, many=True)

        return Response(serializer.data)
     
class NGODetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            ngo = NGO.objects.get(pk=pk, created_by=request.user)
        except NGO.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        serializer = NGOSerializer(ngo)
        return Response(serializer.data)
    
class NGOUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            ngo = NGO.objects.get(pk=pk, created_by=request.user)
        except NGO.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        serializer = NGOSerializer(ngo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

class NGODeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            ngo = NGO.objects.get(pk=pk, created_by=request.user)
        except NGO.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        ngo.delete()
        return Response({"message": "NGO deleted successfully"})