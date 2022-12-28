from django.db import models

class Address(models.Model):
    user = models.ForeignKey("user.User", models.DO_NOTHING)
    street_address = models.CharField(max_length=245)
    city = models.CharField(max_length=245)
    state = models.CharField(max_length=245)
    pincode = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nickname = models.CharField(max_length=50, default=None, blank=True, null=True)
    is_default = models.BooleanField(default = False, null = True, blank=True)