import json

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from polipak_sdk.checklist.factories import get_checklist_client


class ChecklistTemplateCreateView(TemplateView):
    template_name = 'templates_domain/pages/create/page.html'

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        payload = json.loads(request.POST['data'])
        client = get_checklist_client()

        try:
            client.templates.create(data=payload)
            messages.success(request, "Шаблон успешно создан!")
        except Exception as e:
            messages.error(request, f"Ошибка создания: {e}")

        return redirect('templates_domain:template-list')
