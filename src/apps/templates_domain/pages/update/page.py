import json

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.templates_domain.pages.detail.context import get_checklist_template_context
from polipak_sdk.checklist.factories import get_checklist_client


class ChecklistTemplateUpdateView(TemplateView):
    template_name = 'templates_domain/pages/update/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detail_context = get_checklist_template_context(self.kwargs['pk'])
        template_dict = detail_context['template']

        context['template_json'] = json.dumps(template_dict, default=str)
        context['template'] = template_dict
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        payload = json.loads(request.POST['data'])
        client = get_checklist_client()

        try:
            client.templates.update(template_id=self.kwargs['pk'], data=payload)
            messages.success(request, "Шаблон успешно обновлен.")
        except Exception as e:
            messages.error(request, "Ошибка: Невозможно изменить шаблон, по нему уже есть заполненные анкеты.")

        return redirect('templates_domain:template-detail', pk=self.kwargs['pk'])