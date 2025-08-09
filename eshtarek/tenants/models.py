from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=150, unique=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name