from rest_framework import serializers # type: ignore
from .models import NGO

class NGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = '__all__'
        read_only_fields = ['created_by']