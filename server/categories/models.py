from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'