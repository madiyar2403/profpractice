import factory
from factory.django import DjangoModelFactory
from practice.models import User, Contract, Report, Company


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    password = factory.Faker('password')
    username = factory.Faker('last_name')
    first_name = factory.Faker('last_name')
    last_name = factory.Faker('first_name')
    email = factory.Faker('email')
    is_staff = True
    is_active = True
    address = factory.Faker('address')
    birth_date = factory.Faker('date')


class ContractFactory(DjangoModelFactory):
    class Meta:
        model = Contract

    student = factory.SubFactory(UserFactory)
    contract_name = factory.Faker('word')
    contract_type = factory.Faker('word')
    contract_file = factory.Faker('file_name')


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    contract = factory.SubFactory(ContractFactory)
    company_name = factory.Faker('company')
    telephone = factory.Faker('phone_number')
    address = factory.Faker('address')


class ReportFactory(DjangoModelFactory):
    class Meta:
        model = Report

    contract = factory.SubFactory(ContractFactory)
    report_name = factory.Faker('word')
    report_type = factory.Faker('word')
    report_description = factory.Faker('sentence')
    report_file = factory.Faker('file_name')
