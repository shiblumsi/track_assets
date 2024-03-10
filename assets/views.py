from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .models import Organization, Return, Checkout, Device, Employee
from .serializers import OrganizationSerializer, DeviceSerializer, CheckoutSerializer, EmployeeSerializer, \
    ReturnSerializer


class OrganizationCreate(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class EmployeeCreate(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceCreate(CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class CheckoutCreate(CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def perform_create(self, serializer):

        print(serializer.validated_data['device'])

        return serializer


class ReturnCreate(CreateAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer
