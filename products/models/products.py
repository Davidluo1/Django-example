from django.db import models

class Products(models.Model):
    """product"""
    category = models.ForeignKey("products.Categories", models.DO_NOTHING)
    name = models.CharField(max_length=245)
    image = models.CharField(max_length=245)
    price = models.FloatField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'