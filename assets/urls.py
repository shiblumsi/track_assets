from django.urls import path
from .views import OrganizationCreate, EmployeeCreate, DeviceCreate, CheckoutCreate, ReturnCreate

urlpatterns = [
    path('org', OrganizationCreate.as_view(), name='organization-create'),
    path('emp', EmployeeCreate.as_view(), name='employee-create'),
    path('dev', DeviceCreate.as_view(), name='device-create'),
    path('che', CheckoutCreate.as_view(), name='checkout-create'),
    path('ret', ReturnCreate.as_view(), name='return-create'),
]
