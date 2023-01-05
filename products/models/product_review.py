from django.db import models

class ProductReview(models.Model):
    user = models.ForeignKey("user.User", models.DO_NOTHING)
    product = models.ForeignKey("products.Products", models.DO_NOTHING)
    rating = models.FloatField()
    comment = models.CharField(max_length = 1000)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ProductReview'