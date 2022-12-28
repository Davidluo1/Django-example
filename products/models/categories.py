from django.db import models

class Categories(models.Model):
    """Category"""
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'