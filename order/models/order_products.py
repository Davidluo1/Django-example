from django.db import models

class OrderProducts(models.Model):
    order = models.ForeignKey("order.Order", models.DO_NOTHING)
    product = models.ForeignKey("products.Products", models.DO_NOTHING)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)
