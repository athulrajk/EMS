from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class CustomField(models.Model):
    field_name = models.CharField(max_length=50)
    field_type = models.CharField(max_length=20)  # e.g., 'text', 'number', etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    custom_fields = models.ManyToManyField(CustomField, through='EmployeeField')

    def __str__(self):
        return self.user.username

class EmployeeField(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    field = models.ForeignKey(CustomField, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
