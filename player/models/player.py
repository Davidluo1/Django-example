from django.db import models

class Player(models.Model):
    """Player model"""
    country = models.ForeignKey("player.Country", models.DO_NOTHING)
    name = models.CharField(max_length=100)
    image = models.ImageField()
    dob = models.DateField()
    status = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = 'Player'