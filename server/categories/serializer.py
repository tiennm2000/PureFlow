from rest_framework import serializers
from .models import Categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'url_image_category', 'update_at']