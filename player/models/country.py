from django.db import models

class Country(models.Model):
    """Country model"""
    name = models.CharField(max_length=100, null=False, unique=True)
    flag = models.ImageField(null=False)
    continent = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["name","flag", "continent"]
    
    class Meta:
        verbose_name_plural = 'Country'