import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect

from apps.results_domain.pages.create.context import get_checklist_form_context
from polipak_sdk.checklist.factories import get_checklist_client


class ChecklistResultCreateView(TemplateView):
    template_name = 'results_domain/pages/create/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        equipment_uid = self.request.GET.get('equipment_uid')
        checklist_type = self.request.GET.get('checklist_type')

        if equipment_uid and checklist_type:
            try:
                context.update(get_checklist_form_context(equipment_uid, checklist_type))
            except Exception as e:
                messages.error(self.request, "Шаблон не найден")
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Обрабатывает AJAX-запрос от Alpine.js со строгим JSON"""
        try:
            payload = json.loads(request.body)

            client = get_checklist_client()
            client.results.create(data=payload)

            print("[MOCK] Сохранение заполненного чек-листа через Fetch:", payload)

            return JsonResponse({"status": "success", "redirect_url": "/results/"})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Неверный формат JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)