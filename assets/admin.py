from django.contrib import admin
from .models import Organization, Employee, Device, Checkout, Return


class OrganizationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'org_user']


class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'org']
    list_filter = ['org']


class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'configuration', 'status', 'condition', 'org']


class ReturnModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'org_user']

class CheckoutModelAdmin(admin.ModelAdmin):
    list_display = ['employee', 'device', 'status','checkout_date','return_date','org']

admin.site.register(Organization, OrganizationModelAdmin)
admin.site.register(Employee, EmployeeModelAdmin)
admin.site.register(Device, DeviceModelAdmin)
admin.site.register(Checkout, CheckoutModelAdmin)
