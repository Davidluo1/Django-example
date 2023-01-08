from django.db import models

class Match(models.Model):
    """Match model"""
    team_one_id = models.ForeignKey("player.Country", models.DO_NOTHING, related_name="team_white")
    team_two_id = models.ForeignKey("player.Country", models.DO_NOTHING, related_name="team_black")
    match_date = models.TimeField(null=False)
    venue = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = 'Match'