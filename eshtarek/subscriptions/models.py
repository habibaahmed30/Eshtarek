from django.db import models
from tanents.models import Tenant


# Create your models here.
class Plan(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=8,decimal_places=2,default=0)
    max_user=models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    started_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)