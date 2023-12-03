from django.db import models

class Category(models.Model):
    """category"""
    user = models.ForeignKey("user.User", models.DO_NOTHING)
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    logo = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
