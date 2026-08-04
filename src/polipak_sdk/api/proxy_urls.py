from django.urls import re_path

from polipak_sdk.api.views import SERVICE_CLIENTS, ServiceProxyView

services_pattern = '|'.join(SERVICE_CLIENTS.keys())
urlpatterns = [
    re_path(
        rf'^api/(?P<api_version>[^/]+)/integrations/'
        rf'(?P<service>{services_pattern})/'
        rf'(?P<path>.*)$',
        ServiceProxyView.as_view(),
    ),
]
