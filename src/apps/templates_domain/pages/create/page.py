import json
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from polipak_sdk.checklist.factories import get_checklist_client


class ChecklistTemplateCreateView(TemplateView):
    template_name = 'templates_domain/pages/create/page.html'

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Обрабатывает сохранение нового шаблона."""

        payload = json.loads(request.POST['data'])

        # --- ЗАГЛУШКА ---
        # print("[MOCK] Создание нового шаблона:", payload)

        # --- РАБОЧИЙ ВАРИАНТ ---
        client = get_checklist_client()
        client.templates.create(data=payload)

        return redirect('templates_domain:template-list')