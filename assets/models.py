from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Organization(models.Model):
    org_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()


class Employee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Device(models.Model):
    DS = {
        ('AS', 'AS'),
        ('FR', 'FR')
    }
    name = models.CharField(max_length=255)
    configuration = models.TextField()
    status = models.CharField(max_length=2, choices=DS, default='FR')
    condition = models.TextField()
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Checkout(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField()


class Return(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    return_condition = models.TextField()
