from rest_framework import serializers
from .models import Product
from categories.serializer import CategorySerializer
from categories.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'category_id', 'category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'brief_description']