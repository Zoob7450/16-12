from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, PayrollReportViewSet, ContestViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'payrolls', PayrollReportViewSet, basename='payroll')
router.register(r'contests', ContestViewSet, basename='contest')

urlpatterns = [
    path('', include(router.urls)),
]
