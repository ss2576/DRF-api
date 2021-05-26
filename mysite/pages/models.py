from django.db import models

# Create your models here.


class Email(models.Model):
    email = models.EmailField()
    ip_addr = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)

    def save_object(self, data):
        model_email = Email()
        model_email.email = data['email']
        model_email.ip_addr = data['ip_addr']
        model_email.save()
