from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View
from polipak_sdk.checklist.factories import get_checklist_client


class ChecklistTemplateDeleteView(View):
    """
    Обрабатывает удаление шаблона чек-листа.
    Используем View, так как нам нужен только POST метод (без HTML-шаблона).
    """

    def post(self, request: HttpRequest, pk: int, *args, **kwargs) -> HttpResponse:
        # --- РАБОЧИЙ ВАРИАНТ ---
        # client = get_checklist_client()
        # client.templates.delete(template_id=pk)

        # --- ЗАГЛУШКА ---
        print(f"[MOCK] Запрос на удаление шаблона с ID: {pk}")

        return redirect('templates_domain:template-list')