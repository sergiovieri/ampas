from django.db import models


# Create your models here.
class UserGroup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default="")
    discord_server_id = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["-last_activity"]
