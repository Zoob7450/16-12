from rest_framework import viewsets
from .models import Employee, PayrollReport, Contest
from .serializers import EmployeeSerializer, PayrollReportSerializer, ContestSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class PayrollReportViewSet(viewsets.ModelViewSet):
    queryset = PayrollReport.objects.all()
    serializer_class = PayrollReportSerializer

    def perform_create(self, serializer):
        serializer.save()


class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer

    def perform_create(self, serializer):
        serializer.save()
