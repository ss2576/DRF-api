from django.db import models

# Create your models here.


class Parameter(models.Model):
    parameter = models.TextField()
    ip_addr = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
