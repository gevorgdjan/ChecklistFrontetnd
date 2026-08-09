from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View
from polipak_sdk.checklist.factories import get_checklist_client


class ChecklistTemplateDeleteView(View):
    def post(self, request: HttpRequest, pk: int, *args, **kwargs) -> HttpResponse:
        try:
            client = get_checklist_client()
            client.templates.delete(template_id=pk)
            messages.success(request, "Шаблон успешно удален.")
        except Exception as e:
            messages.error(request, "Невозможно удалить шаблон: по нему уже есть заполненные анкеты.")

        return redirect('templates_domain:template-list')