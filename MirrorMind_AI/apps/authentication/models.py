from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    personality_type = models.CharField(max_length=50, blank=True, null=True, help_text="User's personality type")
    mbti_type = models.CharField(max_length=10, blank=True, null=True, help_text="User's MBTI type (for backward compatibility)")
    
    class Meta:
        db_table = 'auth_user'
