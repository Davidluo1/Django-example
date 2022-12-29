from django.db import models

class UserCart(models.Model):
    user = models.ForeignKey("user.User", models.DO_NOTHING)
    product = models.ForeignKey("products.Products", models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'UserCart'