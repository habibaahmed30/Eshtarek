from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
from tenants.models import Tenant


# Create your models here.

class CustomUser(AbstractUser):
    tenant=models.ForeignKey(Tenant,on_delete=CASCADE)
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'
    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_USER, 'Tenant User'),
    ]
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default=ROLE_USER)

    def is_tenant_admin(self):
        return self.role==self.ROLE_ADMIN

