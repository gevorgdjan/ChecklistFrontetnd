from django.views.generic import TemplateView

from apps.results_domain.pages.p_list.context import \
    get_checklist_results_context


class ChecklistResultsListView(TemplateView):
    """Страница со списком анкет чек-листов."""

    template_name = 'results_domain/pages/page_list/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        equipment_uid = self.request.GET.get('equipment_uid')
        user_uid = self.request.GET.get('user_uid')

        context.update(get_checklist_results_context(equipment_uid, user_uid))
        return context
