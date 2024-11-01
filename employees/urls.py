from django.urls import path
from .views import (
    RegisterView, ChangePasswordView, 
    EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView,
    CustomFieldListCreateView, CustomFieldRetrieveUpdateDeleteView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-detail'),
    path('custom-fields/', CustomFieldListCreateView.as_view(), name='custom-field-list-create'),
    path('custom-fields/<int:pk>/', CustomFieldRetrieveUpdateDeleteView.as_view(), name='custom-field-detail'),
]
