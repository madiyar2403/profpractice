from django.contrib import admin
from .models import User, Contract, Company, Report


admin.site.register(User)
admin.site.register(Contract)
admin.site.register(Company)
admin.site.register(Report)
