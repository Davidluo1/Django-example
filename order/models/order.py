from django.db import models

class Order(models.Model):
    user = models.ForeignKey("user.User", models.DO_NOTHING)
    billing_address = models.CharField(max_length=1000)
    shipping_address = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)