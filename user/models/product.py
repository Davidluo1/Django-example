from django.db import models


class Product(models.Model):
    """product"""
    user = models.ForeignKey("user.User", models.DO_NOTHING)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    