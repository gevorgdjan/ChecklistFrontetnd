import requests
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView

from polipak_sdk.base.http_client import HttpClient
from polipak_sdk.checklist.factories import get_checklist_client
from polipak_sdk.jwt_utils.actor import ActorContext

SERVICE_CLIENTS = {
    'checklist': get_checklist_client,
}


class ServiceProxyView(APIView):
    def dispatch(self, request, *args, **kwargs):
        service = kwargs['service']
        api_version = kwargs['api_version']
        path = kwargs.get('path', '')

        client_factory = SERVICE_CLIENTS.get(service)

        if client_factory is None:
            raise Http404()

        client = client_factory()

        try:
            response = self._forward(
                client=client,
                request=request,
                api_version=api_version,
                path=path,
            )

            django_response = HttpResponse(
                response.content,
                status=response.status_code,
            )

            for key, value in response.headers.items():
                if key.lower() not in {
                    'content-length',
                    'transfer-encoding',
                    'connection',
                }:
                    django_response[key] = value

            return django_response

        except requests.RequestException as e:
            return JsonResponse(
                {'detail': (f'Service "{service}" connection error: {e}')},
                status=502,
            )

        except Exception as e:
            return JsonResponse(
                {'detail': str(e)},
                status=500,
            )

    def _clean_headers(self, request):
        return {
            key: value
            for key, value in request.headers.items()
            if key.lower()
            not in [
                'host',
                'content-length',
                'connection',
                'authorization',
            ]
        }

    def _forward(
        self,
        client: HttpClient,
        request,
        api_version: str,
        path: str,
    ):
        target_path = f'api/{api_version}/{path.lstrip("/")}'

        return client.request(
            method=request.method,
            path=target_path,
            actor=ActorContext(type='system'),
            params=request.GET,
            data=request.body,
            headers=self._clean_headers(request),
            files=request.FILES or None,
        )
