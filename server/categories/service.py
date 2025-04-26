from .models import Categories
from django.shortcuts import get_object_or_404


class CategoryService:
    @staticmethod
    def list_categories():
        return Categories.objects.all()
    
    @staticmethod 
    def get_category(pk):
        return get_object_or_404(Categories, pk=pk)
    
    @staticmethod
    def create_category(data):
        return Categories.objects.create(**data)
    
    @staticmethod
    def update_category(pk, data):
        cat = get_object_or_404(Categories, pk=pk)
        for attr, value in data.items():
            setattr(cat, attr, value)
        cat.save()
        return cat
    
    @staticmethod
    def delete_category(pk):
        cat = get_object_or_404(Categories, pk=pk)
        cat.delete()
        return