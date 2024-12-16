from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name


class PayrollReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payroll_reports')
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate total salary before saving
        self.total_salary = self.basic_salary + self.bonus - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.full_name} - {self.month}/{self.year}"


class Contest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    prize = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
