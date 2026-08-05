from django.views.generic import TemplateView

from apps.results_domain.pages.details.context import \
    get_checklist_result_detail_context


class ChecklistResultDetailView(TemplateView):
    template_name = 'results_domain/pages/detail/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_checklist_result_detail_context(self.kwargs['pk']))
        return context
