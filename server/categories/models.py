from django.db import models

class Categories(models.Model):
        name = models.CharField(max_length=100, unique=True)
        url_image_category = models.CharField(max_length=255, blank=False, null=False)
        create_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        
        def __str__(self):
            return self.name
        
        class Meta:
            db_table = 'Categories'