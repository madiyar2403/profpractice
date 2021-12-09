from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=128, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Contract(models.Model):
    student = models.ForeignKey(
        User, related_name='contract', on_delete=models.CASCADE
    )
    contract_name = models.CharField(max_length=128)
    contract_type = models.CharField(max_length=128)
    contract_file = models.FileField(upload_to='uploads/contracts/', blank=True)

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name} {self.contract_name}'


class Company(models.Model):
    contract = models.ForeignKey(
        Contract,
        related_name='company',
        on_delete=models.CASCADE)
    company_name = models.CharField(max_length=128)
    telephone = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.company_name}: {self.contract}'


class Report(models.Model):
    contract = models.OneToOneField(
        Contract, on_delete=models.CASCADE, related_name='report',
        verbose_name='Contract', blank=True, null=True)
    report_name = models.CharField(max_length=128, blank=True, null=True)
    report_type = models.CharField(max_length=128, blank=True, null=True)
    report_description = models.TextField(max_length=2500, null=True, blank=True)
    report_file = models.FileField(upload_to='uploads/reports/', blank=True)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return f'{self.report_name}: {self.contract}'
