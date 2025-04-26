from django.db import models
from django.utils.text import slugify
from categories.models import Category
from unidecode import unidecode

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='products/')
    brief_description = models.CharField(max_length=255)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,related_name='products')
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "product"