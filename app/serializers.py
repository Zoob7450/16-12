from rest_framework import serializers
from .models import Employee, PayrollReport, Contest

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'email', 'phone_number', 'position', 'salary']


class PayrollReportSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = PayrollReport
        fields = ['id', 'employee', 'month', 'year', 'basic_salary', 'bonus', 'deductions', 'total_salary']


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'prize']
