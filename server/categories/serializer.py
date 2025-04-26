from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'create_at', 'update_at']
        read_only_fields = ['id', 'name']
    
    name = serializers.CharField(required=True, allow_blank=False)
    
    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Danh mục đã tồn tại.")
        return value