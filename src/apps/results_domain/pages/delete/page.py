from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.views import View

from polipak_sdk.checklist.factories import get_checklist_client


class ChecklistResultDeleteView(View):
    """
    Обрабатывает удаление заполненной анкеты.
    """

    def post(self, request: HttpRequest, pk: int, *args,
             **kwargs) -> HttpResponse:
        try:
            # --- РАБОЧИЙ ВАРИАНТ ---
            client = get_checklist_client()
            client.results.delete(result_id=pk)

            # print(f"[MOCK] Успешное удаление анкеты {pk}")
            # messages.success(request, "Анкета успешно удалена.")
        except Exception as e:
            messages.error(request, "Ошибка при удалении анкеты.")

        return redirect('results_domain:result-list')