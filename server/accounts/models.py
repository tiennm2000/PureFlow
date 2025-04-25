from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid
from django.utils import timezone


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
        
class PasswordResetToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"ResetToken({self.user.email}, {self.token})"
    
    class Meta:
        db_table = 'PasswordResetToken'