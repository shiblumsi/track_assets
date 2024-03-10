from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Organization(models.Model):
    org_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


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

    def __str__(self) -> str:
        return self.name


class Checkout(models.Model):
    AS = {
        ('IP','IP'),
        ('RE','RE'),
    }
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    status =  models.CharField(max_length=2,choices=AS, default='IP')

    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return self.employee.name


class Return(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    return_condition = models.TextField()

