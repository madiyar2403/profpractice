from django.urls import include, path
from .views import UserApi, UserDetailApi, CompanyApi, CompanyDetailApi, \
    ContractApi, ContractDetailApi, ReportApi, ReportDetailApi


user_patterns = [
    path('', UserApi.as_view()),
    path('<int:pk>/', UserDetailApi.as_view()),
]

company_patterns = [
    path('', CompanyApi.as_view()),
    path('<int:pk>/', CompanyDetailApi.as_view()),
]

contract_patterns = [
    path('', ContractApi.as_view()),
    path('<int:pk>/', ContractDetailApi.as_view()),
]

report_patterns = [
    path('', ReportApi.as_view()),
    path('<int:pk>/', ReportDetailApi.as_view()),
]
