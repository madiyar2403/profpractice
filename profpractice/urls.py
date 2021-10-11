from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from practice.urls import user_patterns, company_patterns, \
    contract_patterns, report_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Example API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('user/', include(user_patterns)),
    path('company/', include(company_patterns)),
    path('contract/', include(contract_patterns)),
    path('report/', include(report_patterns)),
]