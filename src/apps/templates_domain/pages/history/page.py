from django.views.generic import TemplateView

from apps.templates_domain.pages.history.context import get_template_history_context

class ChecklistTemplateHistoryView(TemplateView):
    template_name = 'templates_domain/pages/history/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_template_history_context(self.kwargs['pk']))
        return context
