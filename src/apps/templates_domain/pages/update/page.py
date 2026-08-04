import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.templates_domain.pages.detail.context import get_checklist_template_context
from polipak_sdk.checklist.factories import get_checklist_client


def json_serial(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


class ChecklistTemplateUpdateView(TemplateView):
    template_name = 'template/pages/update/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        detail_context = get_checklist_template_context(self.kwargs['pk'])
        template_dict = detail_context['template']

        context['template_json'] = json.dumps(template_dict, default=json_serial)
        context['template'] = template_dict
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        payload = json.loads(request.POST['data'])

        client = get_checklist_client()
        client.templates.update(
            template_id=self.kwargs['pk'],
            data=payload,
        )

        return redirect(
            'templates_domain:template-detail',
            pk=self.kwargs['pk'],
        )