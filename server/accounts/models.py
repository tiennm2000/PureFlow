from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    role = models.CharField(
        max_length=10,
        choices=[('Admin', 'admin'), ('Customer', 'customer')],
        default='Customer'
    )
    
    phone = models.CharField(max_length=11, unique=True, null=False)
    
    createAt = models.DateField(auto_now_add=True)
    
    status = models.CharField(
        max_length=10,
        choices=[('Active', 'active'), ('Inactive', 'inactive'), ('Block', 'block')],
        default='Active' 
    )
    
    
    def __str__(self):
        return self.username
    
    
    class Meta:
        db_table = 'Users'