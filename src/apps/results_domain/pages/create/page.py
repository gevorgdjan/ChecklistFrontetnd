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

        try:
            client = get_checklist_client()
            context['equipment_list'] = client.templates.get_equipments()
        except Exception:
            context['equipment_list'] = []

        equipment_uid = self.request.GET.get('equipment_uid')
        checklist_type = self.request.GET.get('checklist_type')

        if equipment_uid and checklist_type:
            print(f"[DEBUG] Ищем бланк: UID={equipment_uid}, TYPE={checklist_type}")
            try:
                context.update(get_checklist_form_context(equipment_uid, checklist_type))
                print("[DEBUG] Шаблон успешно добавлен в контекст!")
            except Exception as e:
                print(f"[DEBUG ERROR] Ошибка генерации бланка: {e}")
                messages.error(self.request, str(e))

        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        try:
            payload = json.loads(request.body)

            client = get_checklist_client()
            client.results.create(data=payload)

            return JsonResponse({"status": "success", "redirect_url": "/results/"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
