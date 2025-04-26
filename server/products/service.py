from .models import Product
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from unidecode import unidecode
from django.core.paginator import Paginator, EmptyPage

class ProductService:
    @staticmethod
    def list_product(page=1, page_size=5, category_name=None, min_price=None, max_price=None):
        
        products = Product.objects.all()
        
        if category_name:
            products = products.filter(category__name=category_name)
            
        if min_price is not None:
            products = products.filter(price__gte=min_price)
            
        if max_price is not None:
            products = products.filter(price__lte=max_price)
            
        paginator = Paginator(products, page_size)
        
        try:
            paginated_products= paginator.page(page)
            products_list = paginated_products.object_list
        except EmptyPage:
            products_list = []
            page = 1
        return {
            "products": products_list,
            "total_pages": paginator.num_pages,
            "current_page": page,
            "total_items": paginator.count
        }
    
    @staticmethod
    def get_product_slug(slug):
        return get_object_or_404(Product, slug=slug)
    
    @staticmethod
    def create_product(data):
        return Product.objects.create(**data)
    
    @staticmethod
    def update_product(pk, data):
        pro = get_object_or_404(Product, pk=pk)
        for attr, value in data.items():
            setattr(pro, attr, value)
        if 'name' in data:
            pro.slug = slugify(unidecode(data['name']))
        pro.save()
        return pro
    
    @staticmethod
    def delete_product(pk):
        pro = get_object_or_404(Product, id=pk)
        pro.delete()