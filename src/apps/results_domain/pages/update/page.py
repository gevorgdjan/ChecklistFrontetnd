import json

from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import TemplateView

from apps.results_domain.pages.update.context import get_checklist_result_update_context

from polipak_sdk.checklist.factories import get_checklist_client


class ChecklistResultUpdateView(TemplateView):
    template_name = 'results_domain/pages/update/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context.update(get_checklist_result_update_context(self.kwargs['pk']))
        except Exception as e:
            messages.error(self.request, "Анкета не найдена.")
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Обрабатывает AJAX-запрос от Alpine.js на обновление"""
        try:
            payload = json.loads(request.body)

            # --- РАБОЧИЙ ВАРИАНТ ---
            client = get_checklist_client()
            client.results.update(result_id=self.kwargs['pk'], data=payload)

            # --- ЗАГЛУШКА ---
            # print(f"[MOCK] Обновление анкеты {self.kwargs['pk']}:", payload)

            redirect_url = f"/results/"
            return JsonResponse({"status": "success", "redirect_url": redirect_url})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Неверный формат JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)