from rest_framework import serializers
from .models import Organization, Employee, Device, Checkout, Return


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'description']

    def validate(self, attrs):
        user = self.context['request'].user
        if Organization.objects.filter(org_user=user).exists():
            raise serializers.ValidationError('You can create only one organization!')
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        organization = Organization.objects.create(org_user=user, **validated_data)
        return organization


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        org = Organization.objects.get(org_user=user)
        employee = Employee.objects.create(org=org, **validated_data)
        return employee


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'configuration', 'condition']

    def create(self, validated_data):
        user = self.context['request'].user
        org = Organization.objects.get(org_user=user)
        device = Device.objects.create(org=org, **validated_data)
        return device


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['org', 'employee', 'device', 'return_date']

    def create(self, validated_data):

        user = self.context['request'].user
        org = Organization.objects.get(org_user=user)
        checkout = Checkout.objects.create(org=org, **validated_data)
        return checkout


class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = '__all__'
