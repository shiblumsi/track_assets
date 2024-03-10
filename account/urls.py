from django.urls import path
from .views import OrganizationRegisterCreateView, LoginView

urlpatterns = [
    path('oc', OrganizationRegisterCreateView.as_view(), name='organization-user-create'),
    path('l', LoginView.as_view(), name='login'),
]
