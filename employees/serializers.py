from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee, CustomField, EmployeeField

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class EmployeeSerializer(serializers.ModelSerializer):
    custom_fields = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('id', 'user', 'position', 'custom_fields')

    def get_custom_fields(self, obj):
        return [{field.field_name: field.value} for field in obj.employeefield_set.all()]

class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomField
        fields = ('id', 'field_name', 'field_type')
