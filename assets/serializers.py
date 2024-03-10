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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        org = Organization.objects.get(org_user=user)
        self.fields['employee'].queryset = Employee.objects.filter(org=org)
        self.fields['device'].queryset = Device.objects.filter(org=org, status='FR')
        
    # employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    # employee = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())
    class Meta:
        model = Checkout
        fields = ['employee', 'device', 'return_date']

    def create(self, validated_data):
        user = self.context['request'].user
        org = Organization.objects.get(org_user=user)

        # Update the status of the device
        device = validated_data['device']
        device.status = 'AS'
        device.save()

        checkout = Checkout.objects.create(org=org, **validated_data)
        return checkout


class ReturnSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        org = Organization.objects.get(org_user=user)
        self.fields['employee'].queryset = Employee.objects.filter(org=org,checkout__status='IP')
        self.fields['device'].queryset = Device.objects.filter(org=org, checkout__status='IP')

    class Meta:
        model = Return
        fields = ['employee','device','return_condition']

    def create(self, validated_data):
        user = self.context['request'].user
        org = Organization.objects.get(org_user=user)
        
        dev = validated_data['device']
        dev.status="FR"
        dev.condition=validated_data['return_condition']
        dev.save()
        che_obj = Checkout.objects.get(device=dev)
        che_obj.status='RE'
        che_obj.save()
        return_obj = Return.objects.create(org=org,**validated_data)

        return return_obj
